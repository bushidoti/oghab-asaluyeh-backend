# Generated by Django 4.2.3 on 2023-08-01 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propertyManagement', '0002_alter_person_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='typeProperty',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='type_form',
            field=models.BooleanField(max_length=50, null=True),
        ),
    ]
