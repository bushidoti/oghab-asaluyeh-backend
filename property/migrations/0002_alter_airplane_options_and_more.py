# Generated by Django 4.2.4 on 2023-09-14 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='airplane',
            options={'verbose_name_plural': 'هواپیما'},
        ),
        migrations.AlterModelOptions(
            name='airportequipment',
            options={'verbose_name_plural': 'تجهیزات فرودگاهی'},
        ),
        migrations.AlterModelOptions(
            name='airportfurniture',
            options={'verbose_name_plural': 'اثاث فرودگاهی'},
        ),
        migrations.AlterModelOptions(
            name='airportvehicle',
            options={'verbose_name_plural': 'خودرو فرودگاهی'},
        ),
        migrations.AlterModelOptions(
            name='autoincrementfactor',
            options={'verbose_name_plural': 'شمارنده کد فاکتور'},
        ),
        migrations.AlterModelOptions(
            name='autoincrementproperty',
            options={'verbose_name_plural': 'شمارنده کد ثبت اموال'},
        ),
        migrations.AlterModelOptions(
            name='benefit',
            options={'verbose_name_plural': 'امتیازات'},
        ),
        migrations.AlterModelOptions(
            name='digitalfurniture',
            options={'verbose_name_plural': 'اقلام دیجیتال'},
        ),
        migrations.AlterModelOptions(
            name='electronicfurniture',
            options={'verbose_name_plural': 'اثاث الکترونیکی'},
        ),
        migrations.AlterModelOptions(
            name='facilityfurniture',
            options={'verbose_name_plural': 'اثاث تاسیساتی'},
        ),
        migrations.AlterModelOptions(
            name='factors',
            options={'verbose_name_plural': 'فاکتور ها'},
        ),
        migrations.AlterModelOptions(
            name='industrialtool',
            options={'verbose_name_plural': 'اقلام صنعتی'},
        ),
        migrations.AlterModelOptions(
            name='noneindustrialtool',
            options={'verbose_name_plural': 'اقلام غیر صنعتی'},
        ),
        migrations.AlterModelOptions(
            name='officefurniture',
            options={'verbose_name_plural': 'اثاث اداری'},
        ),
        migrations.AlterModelOptions(
            name='officevehicle',
            options={'verbose_name_plural': 'خودرو اداری'},
        ),
        migrations.AlterModelOptions(
            name='repairedairplane',
            options={'verbose_name_plural': 'تعمیرات هواپیما'},
        ),
        migrations.AlterModelOptions(
            name='repairedairportequipment',
            options={'verbose_name_plural': 'تعمیرات تجهیزات فرودگاهی'},
        ),
        migrations.AlterModelOptions(
            name='repairedairportfurniture',
            options={'verbose_name_plural': 'تعمیرات اثاث فرودگاهی'},
        ),
        migrations.AlterModelOptions(
            name='repairedairportvehicle',
            options={'verbose_name_plural': 'تعمیرات خودرو فرودگاهی'},
        ),
        migrations.AlterModelOptions(
            name='repaireddigitalfurniture',
            options={'verbose_name_plural': 'تعمیرات اقلام دیجیتال'},
        ),
        migrations.AlterModelOptions(
            name='repairedelectronicfurniture',
            options={'verbose_name_plural': 'تعمیرات اثاث الکترونیکی'},
        ),
        migrations.AlterModelOptions(
            name='repairedfacilityfurniture',
            options={'verbose_name_plural': 'تعمیرات اثاث تاسیساتی'},
        ),
        migrations.AlterModelOptions(
            name='repairedindustrialtool',
            options={'verbose_name_plural': 'تعمیرات اقلام صنعتی'},
        ),
        migrations.AlterModelOptions(
            name='repairedofficefurniture',
            options={'verbose_name_plural': 'تعمیرات اثاث اداری'},
        ),
        migrations.AlterModelOptions(
            name='repairedofficevehicle',
            options={'verbose_name_plural': 'تعمیرات خودرو اداری'},
        ),
        migrations.AlterModelOptions(
            name='repairedsafetyequipment',
            options={'verbose_name_plural': 'تعمیرات تجهیزات ایمنی'},
        ),
        migrations.AlterModelOptions(
            name='safetyequipment',
            options={'verbose_name_plural': 'تجهیزات ایمنی'},
        ),
        migrations.AlterModelOptions(
            name='supportitem',
            options={'verbose_name_plural': 'اقلام پشتیبانی'},
        ),
        migrations.AlterField(
            model_name='airplane',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='airplane',
            name='last_handling_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='airportequipment',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='airportequipment',
            name='last_handling_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='airportfurniture',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='airportfurniture',
            name='last_handling_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='airportvehicle',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='airportvehicle',
            name='last_handling_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='benefit',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='benefit',
            name='last_handling_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='digitalfurniture',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='digitalfurniture',
            name='last_handling_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='electronicfurniture',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='electronicfurniture',
            name='last_handling_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='facilityfurniture',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='facilityfurniture',
            name='last_handling_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='factors',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='industrialtool',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='industrialtool',
            name='last_handling_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='noneindustrialtool',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='noneindustrialtool',
            name='last_handling_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='officefurniture',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='officefurniture',
            name='last_handling_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='officevehicle',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='officevehicle',
            name='last_handling_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='repairedairplane',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='repairedairportequipment',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='repairedairportfurniture',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='repairedairportvehicle',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='repaireddigitalfurniture',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='repairedelectronicfurniture',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='repairedfacilityfurniture',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='repairedindustrialtool',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='repairedofficefurniture',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='repairedofficevehicle',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='repairedsafetyequipment',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='safetyequipment',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='safetyequipment',
            name='last_handling_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='supportitem',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='supportitem',
            name='last_handling_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
