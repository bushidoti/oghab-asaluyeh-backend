# Generated by Django 4.2 on 2023-06-15 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_airportequipment_movement_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='airportequipment',
            name='dst_inventory',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='airportfurniture',
            name='dst_inventory',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='airportvehicle',
            name='dst_inventory',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='digitalfurniture',
            name='dst_inventory',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='electronicfurniture',
            name='dst_inventory',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='facilityfurniture',
            name='dst_inventory',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='industrialtool',
            name='dst_inventory',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='noneindustrialtool',
            name='dst_inventory',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='officefurniture',
            name='dst_inventory',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='safetyequipment',
            name='dst_inventory',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='supportitem',
            name='dst_inventory',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
