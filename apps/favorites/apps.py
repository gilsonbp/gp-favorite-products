from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FavoritesConfig(AppConfig):
    name = "apps.favorites"
    label = "favorites"
    verbose_name = _("Favorites")

    def ready(self):
        from . import signals
