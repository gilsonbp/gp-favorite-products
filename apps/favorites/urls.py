from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, FavoriteProductViewSet

app_name = "favorites"


router = DefaultRouter()
router.register("products", ProductViewSet, basename="products")
router.register("favorite-products", FavoriteProductViewSet, basename="favorite-products")

urlpatterns = [
    path("", include(router.urls)),
]
