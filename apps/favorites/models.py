import uuid

from django.db import models
from django.utils.translation import gettext as _
from sorl.thumbnail import ImageField


class CommonModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    class Meta:
        abstract = True
        ordering = ("-created_at",)


class Product(CommonModel):
    title = models.CharField(max_length=250, verbose_name=_("Title"))
    brand = models.CharField(max_length=250, verbose_name=_("Brand"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    image = ImageField(
        upload_to="favorites/product",
        verbose_name=_("Image"),
        help_text=_("Send an image 500x500 pixels or in a proportional size"),
    )
    review_score = models.DecimalField(
        max_digits=10, decimal_places=4, verbose_name=_("Review Score"), default=0
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("title",)
        verbose_name = _("Product")
        verbose_name_plural = _("Product")
