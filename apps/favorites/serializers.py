from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        read_only = ("id", "review_score")
        fields = ("id", "title", "brand", "price", "image", "review_score")
