from django.test import TestCase

from apps.favorites.models import Product
from apps.favorites.serializers import ProductSerializer


class ProductSerializerTestCase(TestCase):
    def setUp(self):
        self.product_attributes = {
            "id": "a683a11e-5758-4bc8-8c59-5fe6d1de047f",
            "title": "Product Test 1",
            "brand": "Brand Test 1",
            "price": "12.99",
            "image": "http://127.0.0.1:8000/media/favorites/product/Screenshot_from_2020-09-19_07-50-37_yJcUHm0.png",
            "review_score": "0.0000",
        }

        self.product = Product.objects.create(**self.product_attributes)
        self.serializer = ProductSerializer(instance=self.product)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {"id", "title", "brand", "price", "image", "review_score"})
