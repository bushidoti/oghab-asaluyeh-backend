# Generated by Django 4.2 on 2023-05-30 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warhouse', '0009_alter_allproducts_document_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='allproducts',
            name='afterOperator',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='allproducts',
            name='beforeOperator',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
