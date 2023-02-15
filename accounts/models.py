from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20)


class Subscriber(CustomUser):
    class Meta:
        proxy = True
        verbose_name = 'مشترک'
        verbose_name_plural = 'مشترکان'


class Staff(CustomUser):
    is_staff = True

    class Meta:
        proxy = True
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسندگان'


class Admin(CustomUser):
    is_staff = True
    is_superuser = True

    class Meta:
        proxy = True
        verbose_name = 'مدیر'
        verbose_name_plural = 'مدیران'