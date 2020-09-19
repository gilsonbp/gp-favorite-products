from django.test import TestCase

from apps.customers.models import Customer
from apps.customers.serializers import CustomerSerializer


class CustomerSerializerTestCase(TestCase):
    def setUp(self):
        self.customer_attributes = {
            "id": "bac591d8-fc84-47d7-af56-6da8e1565a95",
            "email": "test_serializer@test.com",
            "name": "Test Customer",
            "password": "123456",
        }

        self.customer = Customer.objects.create(**self.customer_attributes)
        self.serializer = CustomerSerializer(instance=self.customer)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {"id", "email", "name"})
