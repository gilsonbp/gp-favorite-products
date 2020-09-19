from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from apps.customers.models import Customer


class CustomerAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.customer = Customer.objects.create_customer("test@test.com", "Test Customer")

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(self.customer)

    def test_create_customer(self):
        url = reverse("customers-list")
        data = {
            "email": "test1@test.com",
            "password": "123456",
            "name": "Test1 Customer",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_customers(self):
        url = reverse("customers-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_customer(self):
        url = reverse("customers-detail", kwargs={"pk": self.customer.pk})
        data = {"name": "Test Customer 2"}

        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Customer 2")
