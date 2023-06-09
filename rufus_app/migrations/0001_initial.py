# Generated by Django 4.2 on 2023-05-01 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Dish",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Menu",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="DishItem",
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
                ("name", models.CharField(max_length=255)),
                ("url", models.URLField(blank=True, null=True)),
                ("pictogram_id", models.CharField(max_length=255)),
                (
                    "dishes",
                    models.ManyToManyField(
                        related_name="dish_items", to="rufus_app.dish"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="dish",
            name="menus",
            field=models.ManyToManyField(related_name="dishes", to="rufus_app.menu"),
        ),
    ]
