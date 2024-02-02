from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100, blank=True, null=True)
    rank = models.CharField(max_length=100, blank=True, null=True)
    office = models.CharField(max_length=100, blank=True, null=True)


class Maintenance(models.Model):
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "حالت تعمیر"


class Banner(models.Model):
    message = models.TextField(verbose_name='متن', blank=True, null=True)

    class Meta:
        verbose_name_plural = "متن بنر"
