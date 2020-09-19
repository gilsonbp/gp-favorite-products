from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from apps.customers.tests.factories import CustomerFactory


class CustomerAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.customer = CustomerFactory()

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

    def test_update_password_customer(self):
        url = reverse("customers-detail", kwargs={"pk": self.customer.pk})
        new_password = "654321"
        data = {"password": new_password}

        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        is_auth = self.client.login(email=self.customer.email, password=new_password)
        self.assertEqual(is_auth, True)

    def test_delete_customer(self):
        customer = CustomerFactory(title="Customer Test 3")
        self.client.force_authenticate(customer)

        url = reverse("customers-detail", kwargs={"pk": customer.pk})

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertIsNone(response.data)
