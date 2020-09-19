from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={"input_type": "password"})

    class Meta:
        model = Customer
        read_only = ("id",)
        fields = ("id", "email", "name", "password")

    def create(self, validated_data):
        customer = Customer.objects.create_customer(
            validated_data["email"], validated_data["name"], validated_data["password"],
        )

        return customer

    def update(self, instance, validated_data):
        customer = super(CustomerSerializer, self).update(instance, validated_data)
        password = validated_data.get("password", None)
        if password:
            customer.set_password(validated_data["password"])
            customer.save()
        return customer
