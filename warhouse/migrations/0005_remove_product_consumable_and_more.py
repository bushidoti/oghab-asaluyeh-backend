# Generated by Django 4.2 on 2023-05-26 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warhouse', '0004_product_input_product_output'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='consumable',
        ),
        migrations.RemoveField(
            model_name='product',
            name='number_in_out',
        ),
    ]
