# Generated by Django 4.2 on 2023-06-07 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_alter_airportequipment_year_made_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supportitem',
            name='repaired_status',
        ),
        migrations.AlterField(
            model_name='airportvehicle',
            name='year_changed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='officevehicle',
            name='year_changed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='RepairedSafetyEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('repaired_type', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
                ('safety_equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.safetyequipment')),
            ],
        ),
        migrations.CreateModel(
            name='RepairedOfficeVehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('repaired_type', models.CharField(blank=True, max_length=50, null=True)),
                ('kilometer', models.BigIntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('year_changed', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
                ('office_vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.officevehicle')),
            ],
        ),
        migrations.CreateModel(
            name='RepairedOfficeFurniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
                ('office_furniture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.officefurniture')),
            ],
        ),
        migrations.CreateModel(
            name='RepairedIndustrialTool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
                ('industrial_tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.industrialtool')),
            ],
        ),
        migrations.CreateModel(
            name='RepairedFacilityFurniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
                ('facility_furniture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.facilityfurniture')),
            ],
        ),
        migrations.CreateModel(
            name='RepairedElectronicFurniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
                ('electronic_furniture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.electronicfurniture')),
            ],
        ),
        migrations.CreateModel(
            name='RepairedDigitalFurniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('repaired_type', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
                ('digital_furniture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.digitalfurniture')),
            ],
        ),
        migrations.CreateModel(
            name='RepairedAirportVehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('repaired_type', models.CharField(blank=True, max_length=50, null=True)),
                ('kilometer', models.BigIntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('year_changed', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
                ('airport_vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.airportvehicle')),
            ],
        ),
        migrations.CreateModel(
            name='RepairedAirportFurniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
                ('airport_furniture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.airportfurniture')),
            ],
        ),
        migrations.CreateModel(
            name='RepairedAirportEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('repaired_type', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('airport_equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.airportequipment')),
            ],
        ),
    ]
