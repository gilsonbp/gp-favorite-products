import factory

from apps.customers.models import Customer


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    email = "test0@test.com"
    name = "Customer Test 0"
