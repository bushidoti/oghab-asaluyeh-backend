from django.db import models


class Person(models.Model):
    type = models.CharField(verbose_name='embed',max_length=50, blank=True, null=True)
    full_name = models.CharField(verbose_name='نام کامل',max_length=50, blank=False, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    national_id = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=50, blank=True, null=True)
    extension = models.CharField(max_length=50, blank=True, null=True)
    office = models.CharField(max_length=50, blank=True, null=True)
    job = models.CharField(max_length=50, blank=True, null=True)
    approvedPrice = models.CharField(max_length=50, blank=True, null=True)
    caseNumber = models.CharField(max_length=50, blank=True, null=True)
    commitmentPrice = models.CharField(max_length=50, blank=True, null=True)
    typeBail = models.CharField(max_length=50, blank=True, null=True)
    firstBail = models.CharField(max_length=50, blank=True, null=True)
    secondBail = models.CharField(max_length=50, blank=True, null=True)
    clearedStatus = models.BooleanField(default=False, blank=True, null=True)
    affidavitStatus = models.BooleanField(default=False, blank=True, null=True)
    clearedDate = models.CharField(max_length=50, blank=True, null=True)
    expireDate = models.CharField(max_length=50, blank=True, null=True)
    receivedDocument = models.BooleanField(default=False, blank=True, null=True)
    extended = models.BooleanField(default=False, blank=True, null=True)
    Birth_certificate1 = models.TextField(blank=True, null=True)
    Birth_certificate2 = models.TextField(blank=True, null=True)
    Birth_certificate3 = models.TextField(blank=True, null=True)
    Birth_certificate4 = models.TextField(blank=True, null=True)
    front_card = models.TextField(blank=True, null=True)
    back_card = models.TextField(blank=True, null=True)
    driveLicense = models.TextField(blank=True, null=True)
    bail = models.TextField(blank=True, null=True)
    certificateMedic = models.TextField(blank=True, null=True)
    insurance = models.TextField(blank=True, null=True)
    police = models.TextField(blank=True, null=True)
    retired = models.TextField(blank=True, null=True)
    degreeEducation = models.TextField(blank=True, null=True)
    personalPhoto = models.TextField(blank=True, null=True)
    certificateSecurity = models.TextField(blank=True, null=True)
    retired_insurance = models.TextField(blank=True, null=True)
    retired_card = models.TextField(blank=True, null=True)
    affidavitDoc = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "اشخاص"

class Property(models.Model):
    typeProperty = models.CharField(max_length=50, blank=False, null=True)
    type_form = models.BooleanField(blank=False, null=True, max_length=50)
    name = models.CharField(max_length=50, blank=False, null=True)
    docNumber = models.CharField(max_length=50, blank=True, null=True)
    plateMotor = models.CharField(max_length=50, blank=True, null=True)
    addressChassis = models.CharField(max_length=500, blank=True, null=True)
    landlord = models.CharField(max_length=50, blank=True, null=True)
    modelMeter = models.CharField(max_length=50, blank=True, null=True)
    madeOf = models.CharField(max_length=50, blank=True, null=True)
    part1plate = models.CharField(max_length=2, blank=True, null=True)
    part2plate = models.CharField(max_length=25, blank=True, null=True)
    part3plate = models.CharField(max_length=3, blank=True, null=True)
    cityPlate = models.CharField(max_length=2, blank=True, null=True)
    descriptionLocation = models.CharField(max_length=500, blank=True, null=True)
    paperDoc = models.CharField(max_length=50, blank=True, null=True)
    insurancePaper = models.CharField(max_length=50, blank=True, null=True)
    gasCard = models.CharField(max_length=50, blank=True, null=True)
    carCard = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    soldDate = models.CharField(max_length=50, blank=True, null=True)
    buyer = models.CharField(max_length=50, blank=True, null=True)
    soldStatus =  models.BooleanField(default=False, blank=True, null=True)
    saleFactorFile = models.TextField(blank=True, null=True)
    insurancePaperFile = models.TextField(blank=True, null=True)
    carCardFile = models.TextField(blank=True, null=True)
    greenCardFile = models.TextField(blank=True, null=True)
    gasCardFile = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "اموال"
