from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path, re_path
from django.views import static as url_static
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from apps.customers.views import CustomerViewSet

router = DefaultRouter()
router.register("customers", CustomerViewSet, basename="customers")

urlpatterns = [
    path("", include(router.urls)),
    path("favorites/", include("apps.favorites.urls", namespace="favorites")),
    path("token/", obtain_auth_token),
    re_path(r"^media/(?P<path>.*)$", url_static.serve, {"document_root": settings.MEDIA_ROOT},),
    re_path(r"^static/(?P<path>.*)$", url_static.serve, {"document_root": settings.STATIC_ROOT},),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
