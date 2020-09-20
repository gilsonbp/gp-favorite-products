import uuid

from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
    Permission,
    Group,
)
from django.core import validators
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


class GpPermission(Permission):
    class Meta:
        proxy = True
        verbose_name = _("Permission")
        verbose_name_plural = _("Permissions")


class GpGroup(Group):
    class Meta:
        proxy = True
        verbose_name = _("Group")
        verbose_name_plural = _("Groups")


class CustomerManager(BaseUserManager):
    def create_customer(self, email, name, password=None):
        if not email:
            raise ValueError(_("Customers must have an email."))

        customer = self.model(email=email, name=name,)

        customer.set_password(password)
        customer.save(using=self._db)
        return customer

    def create_superuser(self, email, name, password):
        if not password:
            password = 123456
        customer = self.create_customer(email=email, name=name, password=password,)
        customer.is_superuser = True
        customer.is_staff = True
        customer.save(using=self._db)
        return customer


class Customer(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name=_("Email"),
        unique=True,
        help_text=_("The email will be used to access the system and send information"),
        validators=[validators.EmailValidator()],
        error_messages={"unique": _("This email already exists.")},
    )
    name = models.CharField(
        max_length=200, verbose_name=_("Name"), help_text=_("Enter the customer's full name."),
    )
    is_active = models.BooleanField(
        default=True, verbose_name=_("Active?"), help_text=_("Only active customers can access the system."),
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_("Is part of the team?"),
        help_text=_("Determines whether the customer has access to the system panel."),
    )
    date_joined = models.DateTimeField(_("Registration date"), default=timezone.now)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=True,
        help_text=_(
            "The groups this customer belongs to. A customer will get all permissions "
            "granted to each of their groups."
        ),
        related_name="customers",
        related_query_name="customer",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("customer permissions"),
        blank=True,
        help_text=_("Specific permissions for this customer."),
        related_name="customers",
        related_query_name="customer",
    )

    objects = CustomerManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def clean(self):
        super(Customer, self).clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        return self.name

    get_full_name.short_description = _("Full name")
