import tempfile

from django.urls import reverse
from PIL import Image
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from gpfavoriteproducts.factories import CustomerFactory, ProductFactory, FavoriteProductFactory


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

    def test_list_products(self):
        url = reverse("favorites:products-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_update_product(self):
        url = reverse("favorites:products-detail", kwargs={"pk": self.product.pk})
        data = {"title": "Product Test 1"}

        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], data["title"])

    def test_delete_product(self):
        product = ProductFactory(title="Product Test 2")
        url = reverse("favorites:products-detail", kwargs={"pk": product.pk})

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertIsNone(response.data)


class FavoriteProductAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.customer = CustomerFactory()
        cls.product = ProductFactory()
        cls.favorite_product = FavoriteProductFactory(customer=cls.customer, product=cls.product)

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(self.customer)

    def test_create_favorite_product(self):
        product = ProductFactory()
        url = reverse("favorites:favorite-products-list")
        data = {"product": product.pk}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_favorite_products(self):
        url = reverse("favorites:favorite-products-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
