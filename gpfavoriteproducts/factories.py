from decimal import Decimal

import factory
from django.core.files.base import ContentFile

from apps.customers.models import Customer
from apps.favorites.models import FavoriteProduct, Product


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Sequence(lambda n: "Product Test %s" % n)
    brand = factory.Sequence(lambda n: "Brand Test %s" % n)
    price = Decimal("18.99")
    image = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data({"width": 500, "height": 500}), "image_test.jpg"
        )
    )


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    email = factory.Sequence(lambda n: "test_%s@test.com" % n)
    name = factory.Sequence(lambda n: "Customer Test %s" % n)


class FavoriteProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FavoriteProduct

    customer = factory.SubFactory(CustomerFactory)
    product = factory.SubFactory(ProductFactory)
