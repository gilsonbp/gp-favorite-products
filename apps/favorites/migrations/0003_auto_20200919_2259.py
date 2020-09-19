# Generated by Django 3.1.1 on 2020-09-19 22:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("favorites", "0002_favoriteproduct"),
    ]

    operations = [
        migrations.AlterUniqueTogether(name="favoriteproduct", unique_together={("customer", "product")},),
    ]