from django.test import TestCase

from apps.customers.models import Customer


class CustomerTestCase(TestCase):
    def test_create_customer(self):
        customer = Customer.objects.create_customer("test@test.com", "Test customer")
        self.assertEqual(customer.email, "test@test.com")
        self.assertEqual(customer.name, "Test customer")
