from django.test import TestCase

from apps.favorites.serializers import ProductSerializer
from gpfavoriteproducts.factories import ProductFactory


class ProductSerializerTestCase(TestCase):
    def setUp(self):
        self.product = ProductFactory()
        self.serializer = ProductSerializer(instance=self.product)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {"id", "title", "brand", "price", "image", "review_score"})
