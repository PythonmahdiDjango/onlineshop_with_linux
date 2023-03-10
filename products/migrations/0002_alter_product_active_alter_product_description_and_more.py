# Generated by Django 4.1.4 on 2022-12-23 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="active",
            field=models.BooleanField(default=True, verbose_name="active"),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(verbose_name="description"),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.PositiveIntegerField(default=0, verbose_name="price"),
        ),
        migrations.AlterField(
            model_name="product",
            name="title",
            field=models.CharField(max_length=100, verbose_name="title"),
        ),
    ]
