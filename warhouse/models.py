from django.db import models
from django.core.validators import MaxValueValidator


class Product(models.Model):
    code = models.BigIntegerField("کد ثبت", primary_key=True, unique=True)
    name = models.CharField("نام کالا", max_length=100, blank=False, null=True)
    category = models.CharField("گروه کالا", max_length=50, blank=True, null=True)
    scale = models.CharField("مقیاس", max_length=50, blank=True, null=True)
    inventory = models.CharField("انبار", max_length=50, blank=True, null=True)
    operator = models.CharField("عملیات", max_length=50, blank=True, null=True)
    date = models.CharField("تاریخ", max_length=50, blank=True, null=True)
    input = models.BigIntegerField("ورودی", blank=True, null=True)
    output = models.BigIntegerField("خروجی", blank=True, null=True)
    left_stock = models.BigIntegerField("مانده", default=False, blank=True, null=True)
    document_type = models.CharField("نوع مدرک", max_length=50, blank=True, null=True)
    document_code = models.CharField("شناسه مدرک", max_length=50, blank=True, null=True)
    recycle_status = models.CharField("وضعیت انبارگردانی", max_length=50, blank=True, null=True)
    recycle_date = models.CharField("تاریخ آخرین انبار گردانی", max_length=50, blank=True, null=True)
    description = models.TextField("توضیحت", max_length=50, blank=True, null=True)
    count = models.BigIntegerField("مقدار رویت شده", blank=True, null=True)
    yearly_handling = models.CharField("سال انبارگردانی", max_length=4, blank=True, null=True)

    class Meta:
        verbose_name_plural = "کالا ها"


class FactorsProduct(models.Model):
    code = models.BigIntegerField("کد ثبت", primary_key=True, unique=True)
    inventory = models.CharField("انبار", max_length=50, blank=True, null=True)
    factor = models.TextField("فایل باینری فاکتور", default='', blank=True, null=True)
    jsonData = models.JSONField("کپسول اقلام فاکتور", blank=False, null=True)

    class Meta:
        verbose_name_plural = "فاکتور ها"


class ProductCheck(models.Model):
    code = models.BigIntegerField("کد ثبت", primary_key=True, unique=True)
    inventory = models.CharField("انبار", max_length=50, blank=True, null=True)
    checks = models.TextField("فایل باینری حواله", default='', blank=True, null=True)
    jsonData = models.JSONField("کپسول اقلام حواله", blank=False, null=True)

    class Meta:
        verbose_name_plural = "حواله ها"


class AllProducts(models.Model):
    consumable = models.CharField("مورد مصرف", default='', max_length=50, blank=True, null=True)
    input = models.FloatField("ورودی", blank=True, null=True)
    output = models.FloatField("حروجی", blank=True, null=True)
    afterOperator = models.FloatField("موجودی", blank=True, null=True)
    operator = models.CharField("عملیات", default='', max_length=50, blank=True, null=True)
    scale = models.CharField("مقیاس", default='', max_length=50, blank=True, null=True)
    date = models.CharField("تاریخ", default='', max_length=50, blank=True, null=True)
    buyer = models.CharField("خریدار", default='', max_length=50, blank=True, null=True)
    seller = models.CharField("فروشنده", default='', max_length=50, blank=True, null=True)
    receiver = models.CharField("تحویل گیرنده", default='', max_length=50, blank=True, null=True)
    document_type = models.CharField("نوع مدرک", default='', max_length=50, blank=True, null=True)
    document_code = models.CharField("شناسه مدرک", default='', max_length=150, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="کالای مربوط به")
    factor = models.TextField(default='فاکتور', blank=True, null=True)
    checkBill = models.TextField("حواله", blank=True, null=True)
    factorCode = models.ForeignKey(FactorsProduct, on_delete=models.CASCADE, blank=True, null=True)
    checkCode = models.ForeignKey(ProductCheck, on_delete=models.CASCADE, blank=True, null=True)
    amendment = models.TextField("اصلاحیه", default='', blank=True, null=True)
    obsolete = models.BooleanField("باطل کردن", blank=True, null=True)
    systemID = models.CharField("شماره سیستم", default='', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "گزارش کالا"

    def inventory(self):
        return self.product.inventory

    def name(self):
        return self.product.name

    def category(self):
        return self.product.category

    inventory.short_description = 'انبار'
    category.short_description = 'گروه'
    name.short_description = 'نام کالا'


class Handling(models.Model):
    result = models.TextField(blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "انبارگردانی"


class Consumable(models.Model):
    value = models.CharField("مقدار", max_length=50, blank=True)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name_plural = "مورد مصرف"


class Category(models.Model):
    value = models.CharField("مقدار", max_length=50, blank=True)

    class Meta:
        verbose_name_plural = "گروه"

    def __str__(self):
        return self.value


class AutoIncrement(models.Model):
    oghab101 = models.BigIntegerField(validators=[MaxValueValidator(1019999)], blank=True, null=True)
    oghab102 = models.BigIntegerField(validators=[MaxValueValidator(1029999)], blank=True, null=True)
    oghab103 = models.BigIntegerField(validators=[MaxValueValidator(1039999)], blank=True, null=True)
    oghab104 = models.BigIntegerField(validators=[MaxValueValidator(1049999)], blank=True, null=True)
    oghab105 = models.BigIntegerField(validators=[MaxValueValidator(1059999)], blank=True, null=True)
    oghab106 = models.BigIntegerField(validators=[MaxValueValidator(1069999)], blank=True, null=True)
    oghab107 = models.BigIntegerField(validators=[MaxValueValidator(1079999)], blank=True, null=True)

    class Meta:
        verbose_name_plural = "شمارنده کد ثبت"


class AutoIncrementProduct(models.Model):
    increment = models.BigIntegerField("شمارنده", blank=True, null=True)
    inventory = models.CharField("انبار", max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "شمارنده کد ثبت"


class Transmission(models.Model):
    name = models.CharField("نام کالا", default='', max_length=50, blank=False)
    sender = models.CharField("ارسال کننده", max_length=50, blank=False)
    receiver = models.CharField("دریافت کننده", max_length=50, blank=False)
    input = models.FloatField("تعداد", blank=True, null=True)
    scale = models.CharField("مقیاس", default='', max_length=50, blank=False, null=False)
    date = models.CharField("تاریخ", default='', max_length=50, blank=False, null=False)
    category = models.CharField("گروه", default='', max_length=50, blank=False, null=False)
    systemID = models.CharField("شماره ثبت سیستم", default='', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "انتقالی ها"


class AutoIncrementCheck(models.Model):
    oghab101 = models.BigIntegerField(blank=True, null=True)
    oghab102 = models.BigIntegerField(blank=True, null=True)
    oghab103 = models.BigIntegerField(blank=True, null=True)
    oghab104 = models.BigIntegerField(blank=True, null=True)
    oghab105 = models.BigIntegerField(blank=True, null=True)
    oghab106 = models.BigIntegerField(blank=True, null=True)
    oghab107 = models.BigIntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "شمارنده کد حواله"


class AutoIncrementFactor(models.Model):
    systemID_01 = models.BigIntegerField(blank=True, null=True)
    systemID_02 = models.BigIntegerField(blank=True, null=True)
    systemID_03 = models.BigIntegerField(blank=True, null=True)
    systemID_04 = models.BigIntegerField(blank=True, null=True)
    systemID_05 = models.BigIntegerField(blank=True, null=True)
    systemID_06 = models.BigIntegerField(blank=True, null=True)
    systemID_07 = models.BigIntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "شمارنده کد فاکتور"


class AutoIncrementProductFactor(models.Model):
    increment = models.BigIntegerField("شمارنده", blank=True, null=True)
    inventory = models.CharField("انبار", max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "شمارنده کد فاکتور"


class AutoIncrementProductCheck(models.Model):
    increment = models.BigIntegerField("شمارنده", blank=True, null=True)
    inventory = models.CharField("انبار", max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "شمارنده کد حواله"
