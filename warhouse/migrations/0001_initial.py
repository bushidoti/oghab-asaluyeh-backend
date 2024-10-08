# Generated by Django 4.2.7 on 2024-02-23 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutoIncrementProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('increment', models.BigIntegerField(blank=True, null=True, verbose_name='شمارنده')),
                ('inventory', models.CharField(blank=True, max_length=50, null=True, verbose_name='انبار')),
            ],
            options={
                'verbose_name_plural': 'شمارنده کد ثبت',
            },
        ),
        migrations.CreateModel(
            name='AutoIncrementProductCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('increment', models.BigIntegerField(blank=True, null=True, verbose_name='شمارنده')),
                ('inventory', models.CharField(blank=True, max_length=50, null=True, verbose_name='انبار')),
            ],
            options={
                'verbose_name_plural': 'شمارنده کد حواله',
            },
        ),
        migrations.CreateModel(
            name='AutoIncrementProductFactor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('increment', models.BigIntegerField(blank=True, null=True, verbose_name='شمارنده')),
                ('inventory', models.CharField(blank=True, max_length=50, null=True, verbose_name='انبار')),
            ],
            options={
                'verbose_name_plural': 'شمارنده کد فاکتور',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=50, verbose_name='مقدار')),
            ],
            options={
                'verbose_name_plural': 'گروه',
            },
        ),
        migrations.CreateModel(
            name='Consumable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=50, verbose_name='مقدار')),
            ],
            options={
                'verbose_name_plural': 'مورد مصرف',
            },
        ),
        migrations.CreateModel(
            name='FactorsProduct',
            fields=[
                ('code', models.BigIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='کد ثبت')),
                ('inventory', models.CharField(blank=True, max_length=50, null=True, verbose_name='انبار')),
                ('factor', models.TextField(blank=True, default='', null=True, verbose_name='فایل باینری فاکتور')),
                ('jsonData', models.JSONField(null=True, verbose_name='کپسول اقلام فاکتور')),
            ],
            options={
                'verbose_name_plural': 'فاکتور ها',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('code', models.BigIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='کد ثبت')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='نام کالا')),
                ('category', models.CharField(blank=True, max_length=50, null=True, verbose_name='گروه کالا')),
                ('scale', models.CharField(blank=True, max_length=50, null=True, verbose_name='مقیاس')),
                ('inventory', models.CharField(blank=True, max_length=50, null=True, verbose_name='انبار')),
                ('recycle_status', models.CharField(blank=True, max_length=50, null=True, verbose_name='وضعیت انبارگردانی')),
                ('recycle_date', models.CharField(blank=True, max_length=50, null=True, verbose_name='تاریخ آخرین انبار گردانی')),
                ('description', models.TextField(blank=True, max_length=50, null=True, verbose_name='توضیحت')),
                ('count', models.BigIntegerField(blank=True, null=True, verbose_name='مقدار رویت شده')),
                ('yearly_handling', models.CharField(blank=True, max_length=4, null=True, verbose_name='سال انبارگردانی')),
            ],
            options={
                'verbose_name_plural': 'کالا ها',
            },
        ),
        migrations.CreateModel(
            name='ProductCheck',
            fields=[
                ('code', models.BigIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='کد ثبت')),
                ('inventory', models.CharField(blank=True, max_length=50, null=True, verbose_name='انبار')),
                ('checks', models.TextField(blank=True, default='', null=True, verbose_name='فایل باینری حواله')),
                ('jsonData', models.JSONField(null=True, verbose_name='کپسول اقلام حواله')),
            ],
            options={
                'verbose_name_plural': 'حواله ها',
            },
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='نام کالا')),
                ('sender', models.CharField(max_length=50, verbose_name='ارسال کننده')),
                ('receiver', models.CharField(max_length=50, verbose_name='دریافت کننده')),
                ('input', models.FloatField(blank=True, null=True, verbose_name='تعداد')),
                ('scale', models.CharField(default='', max_length=50, verbose_name='مقیاس')),
                ('date', models.CharField(default='', max_length=50, verbose_name='تاریخ')),
                ('category', models.CharField(default='', max_length=50, verbose_name='گروه')),
                ('systemID', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='شماره ثبت سیستم')),
            ],
            options={
                'verbose_name_plural': 'انتقالی ها',
            },
        ),
        migrations.CreateModel(
            name='Handling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.TextField(blank=True, null=True)),
                ('date', models.CharField(blank=True, max_length=50, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warhouse.product')),
            ],
            options={
                'verbose_name_plural': 'انبارگردانی',
            },
        ),
        migrations.CreateModel(
            name='AllProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumable', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='مورد مصرف')),
                ('input', models.FloatField(blank=True, null=True, verbose_name='ورودی')),
                ('output', models.FloatField(blank=True, null=True, verbose_name='حروجی')),
                ('afterOperator', models.FloatField(blank=True, null=True, verbose_name='موجودی')),
                ('operator', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='عملیات')),
                ('date', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='تاریخ')),
                ('buyer', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='خریدار')),
                ('seller', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='فروشنده')),
                ('receiver', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='تحویل گیرنده')),
                ('document_type', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='نوع مدرک')),
                ('document_code', models.CharField(blank=True, default='', max_length=150, null=True, verbose_name='شناسه مدرک')),
                ('amendment', models.TextField(blank=True, default='', null=True, verbose_name='اصلاحیه')),
                ('obsolete', models.BooleanField(blank=True, null=True, verbose_name='باطل کردن')),
                ('systemID', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='شماره سیستم')),
                ('checkCode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='warhouse.productcheck')),
                ('factorCode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='warhouse.factorsproduct')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warhouse.product', verbose_name='کالای مربوط به')),
            ],
            options={
                'verbose_name_plural': 'گزارش کالا',
            },
        ),
    ]
