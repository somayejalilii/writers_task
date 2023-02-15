from django.contrib import admin
from .models import Subscriber, CustomUser, Staff, Admin

# Register your models here.
admin.site.register(Subscriber)
admin.site.register(CustomUser)
admin.site.register(Staff)
admin.site.register(Admin)
