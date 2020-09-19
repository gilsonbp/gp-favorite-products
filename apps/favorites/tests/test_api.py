import tempfile

from PIL import Image
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from apps.favorites.tests.factories import ProductFactory, CustomerFactory


class ProductAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.customer = CustomerFactory()
        cls.product = ProductFactory()

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(self.customer)

    @staticmethod
    def generate_image():
        tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg")
        image = Image.new("RGB", (100, 100))
        image.save(tmp_file.name)
        return tmp_file

    def test_create_product(self):
        url = reverse("favorites:products-list")
        data = {
            "title": "Product Test 1",
            "brand": "Brand Test 1",
            "price": "12.99",
            "image": self.generate_image(),
        }
        response = self.client.post(url, data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
