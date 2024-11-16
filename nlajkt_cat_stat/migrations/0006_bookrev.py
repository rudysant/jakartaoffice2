# Generated by Django 4.1.1 on 2023-08-29 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "nlajkt_cat_stat",
            "0005_alter_cat_cons_add_vol_alter_cat_cons_end_date_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="BookRev",
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
                ("entrydate", models.DateField()),
                ("title", models.CharField(max_length=200)),
                ("author", models.CharField(max_length=100)),
                ("isbn", models.CharField(max_length=20)),
                ("publication", models.CharField(max_length=200)),
                ("paging", models.CharField(max_length=100)),
                ("summary", models.TextField()),
                ("cover", models.ImageField(upload_to="media")),
            ],
        ),
    ]