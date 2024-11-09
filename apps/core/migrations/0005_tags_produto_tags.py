# Generated by Django 5.1.2 on 2024-11-05 16:40

import django.db.models.deletion
import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_remove_produto_tags_delete_tags"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tags",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tId",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefgh1234567",
                        length=10,
                        max_length=20,
                        prefix="teg",
                        unique=True,
                    ),
                ),
                ("title", models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name="produto",
            name="tags",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="core.tags"
            ),
        ),
    ]
