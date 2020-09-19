from decimal import Decimal

import factory
from django.core.files.base import ContentFile

from apps.customers.models import Customer
from apps.favorites.models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    title = "Product Test 0"
    brand = "Brand Test 0"
    price = Decimal("18.99")
    image = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data({"width": 500, "height": 500}), "image_test.jpg"
        )
    )


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    email = "test0@test.com"
    name = "Customer Test 0"
