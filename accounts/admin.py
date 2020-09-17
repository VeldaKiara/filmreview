from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from accounts.models import CustomUser

# Register your models here.
admin.site.register(CustomUser, UserAdmin)