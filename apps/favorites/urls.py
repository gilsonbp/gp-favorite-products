from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet

app_name = "favorites"


router = DefaultRouter()
router.register("products", ProductViewSet, basename="products")

urlpatterns = [
    path("", include(router.urls)),
]
