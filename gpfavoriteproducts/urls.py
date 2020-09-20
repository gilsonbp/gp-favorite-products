from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path, re_path
from django.views import static as url_static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from apps.customers.views import CustomerViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="GP Favorite Products API",
        default_version="v1",
        description="GP Favorite Products API",
        terms_of_service="http://gilsonpaulino.dev",
        contact=openapi.Contact(email="gilsonbp@gmail.com"),
        license=openapi.License(name="GNU General Public License v3.0"),
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)

router = DefaultRouter()
router.register("customers", CustomerViewSet, basename="customers")

urlpatterns = [
    path("", include(router.urls)),
    path("favorites/", include("apps.favorites.urls", namespace="favorites")),
    path("token/", obtain_auth_token),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json",
    ),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui",),
    re_path(r"^media/(?P<path>.*)$", url_static.serve, {"document_root": settings.MEDIA_ROOT},),
    re_path(r"^static/(?P<path>.*)$", url_static.serve, {"document_root": settings.STATIC_ROOT},),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
