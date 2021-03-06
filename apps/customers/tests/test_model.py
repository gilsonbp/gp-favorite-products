from django.test import TestCase
from django.db import IntegrityError
from apps.customers.models import Customer


class CustomerTestCase(TestCase):
    def test_create_customer(self):
        customer = Customer.objects.create_customer("test@test.com", "Test customer")
        self.assertEqual(customer.email, "test@test.com")
        self.assertEqual(customer.name, "Test customer")

    def test_create_customer_without_email(self):
        with self.assertRaises(ValueError):
            Customer.objects.create_customer(email=None, name="User test")

    def test_customer_full_name(self):
        customer = Customer.objects.create_customer("test@test.com", "Test customer")
        self.assertEqual(customer.get_full_name(), "Test customer")

    def test_create_superuser(self):
        customer = Customer.objects.create_superuser("super@test.com", "Test Super User", "123456")
        self.assertEqual(customer.email, "super@test.com")
        self.assertEqual(customer.name, "Test Super User")
        self.assertEqual(customer.is_superuser, True)

    def test_update_empty_password(self):
        customer = Customer.objects.create_customer("test2@test.com", "Test customer 2", "123456")

        with self.assertRaises(IntegrityError):
            customer.password = None
            customer.save()

    def test_create_customer_with_existing_email(self):
        Customer.objects.create_customer("test@test.com", "Test customer", "123456")

        with self.assertRaises(IntegrityError):
            Customer.objects.create_customer("test@test.com", "Test customer 2", "123456")
