# Generated by Django 4.1.1 on 2022-10-13 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
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
                ("weight_kg", models.IntegerField()),
                ("height_cm", models.IntegerField()),
                ("gender", models.CharField(max_length=1)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Food",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("energy_kcal", models.IntegerField()),
                ("proteins_g", models.FloatField()),
                ("lipids_g", models.FloatField()),
                ("carbohydrates_g", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Meal",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("date", models.DateField()),
                (
                    "id_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="it.client"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Quantity",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("gram", models.IntegerField()),
                (
                    "id_food",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="it.food"
                    ),
                ),
                (
                    "id_meal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="it.meal"
                    ),
                ),
            ],
        ),
    ]
