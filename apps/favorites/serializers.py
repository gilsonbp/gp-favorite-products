from rest_framework import serializers

from .models import Product, FavoriteProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        read_only = ("id", "review_score")
        fields = ("id", "title", "brand", "price", "image", "review_score")


class FavoriteProductSerializer(serializers.ModelSerializer):
    customer = serializers.UUIDField(write_only=True, default=serializers.CurrentUserDefault())
    title = serializers.CharField(read_only=True, source="product.title")
    image = serializers.CharField(read_only=True, source="product.image.url")
    price = serializers.DecimalField(read_only=True, source="product.price", max_digits=12, decimal_places=2)

    class Meta:
        model = FavoriteProduct
        fields = ("customer", "product", "title", "image", "price")
