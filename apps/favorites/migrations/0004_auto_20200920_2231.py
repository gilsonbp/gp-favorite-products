# Generated by Django 3.1.1 on 2020-09-20 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("favorites", "0003_auto_20200919_2259"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="favoriteproduct",
            options={
                "ordering": ("-created_at",),
                "verbose_name": "Favorite Product",
                "verbose_name_plural": "Favorite Products",
            },
        ),
    ]
