from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.favorites.models import FavoriteProduct


@receiver(post_save, sender=FavoriteProduct)
def review_score(sender, instance, **kwargs):
    if kwargs["created"]:
        total_favorites = FavoriteProduct.objects.count()
        total_product_favorites = FavoriteProduct.objects.filter(product=instance.product).count()
        average = total_favorites / total_product_favorites
        instance.product.review_score = average
        instance.product.save()
