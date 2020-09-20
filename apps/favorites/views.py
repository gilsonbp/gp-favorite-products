from rest_framework import viewsets, mixins

from .models import Product, FavoriteProduct
from .serializers import ProductSerializer, FavoriteProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class FavoriteProductViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    serializer_class = FavoriteProductSerializer
    queryset = FavoriteProduct.objects.all()

    def get_queryset(self):
        qs = super(FavoriteProductViewSet, self).get_queryset()
        return qs.filter(customer=self.request.user)
