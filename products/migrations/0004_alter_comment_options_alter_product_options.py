# Generated by Django 4.1.4 on 2022-12-25 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_comment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"verbose_name": "comment", "verbose_name_plural": "comments"},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "product", "verbose_name_plural": "products"},
        ),
    ]
