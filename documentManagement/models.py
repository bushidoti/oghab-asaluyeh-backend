from django.db import models


class Document(models.Model):
    contractNumber = models.CharField("شماره قرارداد", max_length=500, blank=True, null=True)
    name = models.CharField("نام", blank=True, null=True, max_length=50)
    office = models.CharField("محل کار", max_length=50, blank=True, null=True)
    type_form = models.CharField("نوع فرم", blank=True, null=True, max_length=50)
    dateContract = models.CharField("تاریخ قرارداد", max_length=50, blank=True, null=True)
    contractPrice = models.CharField("مبلغ قرارداد", max_length=50, blank=True, null=True)
    durationContract = models.CharField("مدت قرارداد", max_length=50, blank=True, null=True)
    prePaidPrice = models.CharField("مبلغ پیش پرداخت", max_length=50, blank=True, null=True)
    goodPrice = models.CharField("مبلغ حسن انجام کار", max_length=50, blank=True, null=True)
    typeBail1 = models.CharField("نوع ضمانت", max_length=50, blank=True, null=True)
    firstBail = models.CharField("مشخصه ضمانت", max_length=50, blank=True, null=True)
    secondBail = models.CharField("مشخصه ضمانت", max_length=50, blank=True, null=True)
    commitmentPrice = models.CharField("مبلغ تعهد انجام کار", max_length=50, blank=True, null=True)
    typeBail2 = models.CharField("نوع ضمانت", max_length=50, blank=True, null=True)
    firstBail2 = models.CharField("مشخصه ضمانت", max_length=50, blank=True, null=True)
    secondBail2 = models.CharField("مشخصه ضمانت", max_length=50, blank=True, null=True)
    topicContract = models.CharField("موضوع قرارداد", max_length=50, blank=True, null=True)
    typeContract = models.CharField("نوع قرارداد", max_length=50, blank=True, null=True)
    clearedDate = models.CharField("تاریخ تسویه", max_length=50, blank=True, null=True)
    receivedDocument = models.BooleanField("وضعیت مدرک", default=False, blank=True, null=True)
    clearedStatus = models.BooleanField("وضعیت تسویه", default=False, blank=True, null=True)
    doc_1 = models.TextField(blank=True, null=True)
    doc_2 = models.TextField(blank=True, null=True)
    doc_3 = models.TextField(blank=True, null=True)
    doc_4 = models.TextField(blank=True, null=True)
    doc_5 = models.TextField(blank=True, null=True)
    doc_6 = models.TextField(blank=True, null=True)
    doc_7 = models.TextField(blank=True, null=True)
    doc_8 = models.TextField(blank=True, null=True)
    doc_9 = models.TextField(blank=True, null=True)
    doc_10 = models.TextField(blank=True, null=True)
    doc_bail_1 = models.TextField(blank=True, null=True)
    doc_bail_2 = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "قرارداد ها"

    def _str_(self):
        return self.contractNumber
