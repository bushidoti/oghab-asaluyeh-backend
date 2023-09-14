from django.db import models


class Document(models.Model):
    contractNumber = models.CharField(max_length=500, blank=True, null=True)
    employer = models.CharField(blank=True, null=True, max_length=50)
    type_form = models.BooleanField(blank=True, null=True, max_length=50)
    dateContract = models.CharField(max_length=50, blank=True, null=True)
    contractPrice = models.CharField(max_length=50, blank=True, null=True)
    durationContract = models.CharField(max_length=50, blank=True, null=True)
    prePaidPrice = models.CharField(max_length=50, blank=True, null=True)
    goodPrice = models.CharField(max_length=50, blank=True, null=True)
    typeBail1 = models.CharField(max_length=50, blank=True, null=True)
    firstBail = models.CharField(max_length=50, blank=True, null=True)
    secondBail = models.CharField(max_length=50, blank=True, null=True)
    commitmentPrice = models.CharField(max_length=50, blank=True, null=True)
    typeBail2 = models.CharField(max_length=50, blank=True, null=True)
    firstBail2 = models.CharField(max_length=50, blank=True, null=True)
    secondBail2 = models.CharField(max_length=50, blank=True, null=True)
    topicContract = models.CharField(max_length=50, blank=True, null=True)
    typeContract = models.CharField(max_length=50, blank=True, null=True)
    clearedDate = models.CharField(max_length=50, blank=True, null=True)
    receivedDocument = models.BooleanField(default=False, blank=True, null=True)
    clearedStatus = models.BooleanField(default=False, blank=True, null=True)
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
