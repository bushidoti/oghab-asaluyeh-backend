# Generated by Django 4.2 on 2023-06-02 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warhouse', '0013_product_obsolete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='obsolete',
        ),
        migrations.AddField(
            model_name='allproducts',
            name='obsolete',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
