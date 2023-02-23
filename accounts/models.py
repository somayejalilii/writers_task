from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


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


class Article(models.Model):
    RELEASE = [('Publish', 'Publish'), ('Draft', 'Draft')]
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    release_mode = models.CharField(max_length=10, choices=RELEASE, default='Draft')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    release_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='article_image/')


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile/', null=True, blank=True)

    def __str__(self):
        return self.user.username


def save_profile_user(sender, **kwargs):
    if kwargs['created']:
        profile_user = Profile(user=kwargs['instance'])
        profile_user.save()


post_save.connect(save_profile_user, sender=CustomUser)
