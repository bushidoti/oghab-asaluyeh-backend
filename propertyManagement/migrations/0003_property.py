# Generated by Django 4.2 on 2023-05-07 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propertyManagement', '0002_delete_property'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typePropertySelector', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('docNumber', models.CharField(max_length=50, unique=True)),
                ('plateMotor', models.CharField(max_length=50)),
                ('addressChassis', models.CharField(max_length=50)),
                ('landlord', models.CharField(max_length=50)),
                ('modelMeter', models.CharField(max_length=50)),
                ('madeOf', models.CharField(max_length=50)),
                ('carPlate', models.CharField(max_length=50)),
                ('descriptionLocation', models.CharField(max_length=500)),
                ('paperDoc', models.CharField(max_length=50)),
                ('insurancePaper', models.CharField(max_length=50)),
                ('gasCard', models.CharField(max_length=50)),
                ('carCard', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('soldDatePicker', models.DateField()),
                ('buyer', models.CharField(max_length=50)),
                ('soledStatus', models.BooleanField(default=False)),
            ],
        ),
    ]
