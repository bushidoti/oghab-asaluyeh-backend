# Generated by Django 4.2 on 2023-05-19 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('propertyManagement', '0010_alter_property_carplate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='carPlate',
        ),
    ]
