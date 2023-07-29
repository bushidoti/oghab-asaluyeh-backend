# Generated by Django 4.2 on 2023-07-29 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
                ('full_name', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('national_id', models.CharField(blank=True, max_length=50, null=True)),
                ('sex', models.CharField(blank=True, max_length=50, null=True)),
                ('office', models.CharField(blank=True, max_length=50, null=True)),
                ('job', models.CharField(blank=True, max_length=50, null=True)),
                ('approvedPrice', models.CharField(blank=True, max_length=50, null=True)),
                ('commitmentPrice', models.CharField(blank=True, max_length=50, null=True)),
                ('typeBail', models.CharField(blank=True, max_length=50, null=True)),
                ('firstBail', models.CharField(blank=True, max_length=50, null=True)),
                ('secondBail', models.CharField(blank=True, max_length=50, null=True)),
                ('clearedStatus', models.BooleanField(blank=True, default=False, null=True)),
                ('clearedDate', models.DateField(blank=True, null=True)),
                ('receivedDocument', models.BooleanField(blank=True, default=False, null=True)),
                ('Birth_certificate1', models.TextField(blank=True, null=True)),
                ('Birth_certificate2', models.TextField(blank=True, null=True)),
                ('Birth_certificate3', models.TextField(blank=True, null=True)),
                ('Birth_certificate4', models.TextField(blank=True, null=True)),
                ('front_card', models.TextField(blank=True, null=True)),
                ('back_card', models.TextField(blank=True, null=True)),
                ('driveLicense', models.TextField(blank=True, null=True)),
                ('bail', models.TextField(blank=True, null=True)),
                ('certificateMedic', models.TextField(blank=True, null=True)),
                ('insurance', models.TextField(blank=True, null=True)),
                ('police', models.TextField(blank=True, null=True)),
                ('retired', models.TextField(blank=True, null=True)),
                ('retired_card', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeProperty', models.CharField(blank=True, max_length=50, null=True)),
                ('type_form', models.BooleanField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('docNumber', models.CharField(blank=True, max_length=50, null=True)),
                ('plateMotor', models.CharField(blank=True, max_length=50, null=True)),
                ('addressChassis', models.CharField(blank=True, max_length=500, null=True)),
                ('landlord', models.CharField(blank=True, max_length=50, null=True)),
                ('modelMeter', models.CharField(blank=True, max_length=50, null=True)),
                ('madeOf', models.CharField(blank=True, max_length=50, null=True)),
                ('part1plate', models.CharField(blank=True, max_length=2, null=True)),
                ('part2plate', models.CharField(blank=True, max_length=1, null=True)),
                ('part3plate', models.CharField(blank=True, max_length=3, null=True)),
                ('cityPlate', models.CharField(blank=True, max_length=2, null=True)),
                ('descriptionLocation', models.CharField(blank=True, max_length=500, null=True)),
                ('paperDoc', models.CharField(blank=True, max_length=50, null=True)),
                ('insurancePaper', models.CharField(blank=True, max_length=50, null=True)),
                ('gasCard', models.CharField(blank=True, max_length=50, null=True)),
                ('carCard', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('soldDate', models.DateField(blank=True, null=True)),
                ('buyer', models.CharField(blank=True, max_length=50, null=True)),
                ('soldStatus', models.BooleanField(blank=True, default=False, null=True)),
                ('saleFactorFile', models.TextField(blank=True, null=True)),
                ('insurancePaperFile', models.TextField(blank=True, null=True)),
                ('carCardFile', models.TextField(blank=True, null=True)),
                ('greenCardFile', models.TextField(blank=True, null=True)),
                ('gasCardFile', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
