# Generated by Django 4.2.4 on 2023-09-14 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propertyManagement', '0005_person_affidavitdoc_person_affidavitstatus_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'اشخاص'},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name_plural': 'اموال'},
        ),
        migrations.AlterField(
            model_name='person',
            name='clearedDate',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='full_name',
            field=models.CharField(max_length=50, null=True, verbose_name='نام کامل'),
        ),
        migrations.AlterField(
            model_name='person',
            name='type',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='embed'),
        ),
        migrations.AlterField(
            model_name='property',
            name='soldDate',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
