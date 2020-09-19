from django.test import TestCase

from apps.customers.models import Customer


class CustomerTestCase(TestCase):
    def test_create_customer(self):
        customer = Customer.objects.create_customer("test@test.com", "Test customer")
        self.assertEqual(customer.email, "test@test.com")
        self.assertEqual(customer.name, "Test customer")

    def test_create_superuser(self):
        customer = Customer.objects.create_superuser("super@test.com", "Test Super User", "123456")
        self.assertEqual(customer.email, "super@test.com")
        self.assertEqual(customer.name, "Test Super User")
        self.assertEqual(customer.is_superuser, True)