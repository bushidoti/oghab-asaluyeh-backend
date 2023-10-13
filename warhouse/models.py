from django.db import models
from django.core.validators import MaxValueValidator


class Product(models.Model):
    code = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, blank=False, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    scale = models.CharField(max_length=50, blank=True, null=True)
    inventory = models.CharField(max_length=50, blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    input = models.BigIntegerField(blank=True, null=True)
    output = models.BigIntegerField(blank=True, null=True)
    left_stock = models.BigIntegerField(default=False, blank=True, null=True)
    document_type = models.CharField(max_length=50, blank=True, null=True)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    recycle_status = models.CharField(max_length=50, blank=True, null=True)
    recycle_date = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    count = models.BigIntegerField(blank=True, null=True)
    yearly_handling = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        verbose_name_plural = "کالا ها"


class AllProducts(models.Model):
    consumable = models.CharField(default='', max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=False, null=True)
    input = models.FloatField(blank=True, null=True)
    output = models.FloatField(blank=True, null=True)
    afterOperator = models.FloatField(blank=True, null=True)
    operator = models.CharField(default='', max_length=50, blank=True, null=True)
    scale = models.CharField(default='', max_length=50, blank=True, null=True)
    date = models.CharField(default='', max_length=50, blank=True, null=True)
    buyer = models.CharField(default='', max_length=50, blank=True, null=True)
    seller = models.CharField(default='', max_length=50, blank=True, null=True)
    receiver = models.CharField(default='', max_length=50, blank=True, null=True)
    document_type = models.CharField(default='', max_length=50, blank=True, null=True)
    document_code = models.CharField(default='', max_length=50, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    factor = models.TextField(default='', blank=True, null=True)
    checkBill = models.TextField(default='', blank=True, null=True)
    amendment = models.TextField(default='', blank=True, null=True)
    obsolete = models.BooleanField(blank=True, null=True)
    systemID = models.CharField(default='', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "گزارش کالا ها"

    def inventory(self):
        return self.product.inventory

    def category(self):
        return self.product.category


class Handling(models.Model):
    result = models.TextField(blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "انبارداری"


class Consumable(models.Model):
    value = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name_plural = "مورد مصرف"


class Category(models.Model):
    value = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name_plural = "گروه"


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
    increment = models.BigIntegerField(blank=True, null=True)
    inventory = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "شمارنده کد ثبت"


class FactorsProduct(models.Model):
    code = models.BigIntegerField(primary_key=True, unique=True)
    inventory = models.CharField(max_length=50, blank=True, null=True)
    factor = models.TextField(default='', blank=True, null=True)

    class Meta:
        verbose_name_plural = "فاکتور ها"


class ProductCheck(models.Model):
    code = models.BigIntegerField(primary_key=True, unique=True)
    inventory = models.CharField(max_length=50, blank=True, null=True)
    checks = models.TextField(default='', blank=True, null=True)

    class Meta:
        verbose_name_plural = "فاکتور ها"


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
    increment = models.BigIntegerField(blank=True, null=True)
    inventory = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "شمارنده کد فاکتور"


class AutoIncrementProductCheck(models.Model):
    increment = models.BigIntegerField(blank=True, null=True)
    inventory = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "شمارنده کد حواله"
