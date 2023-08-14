
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

class CustomUserAdmin(UserAdmin):
      list_display = ('pk','phonenumber')

admin.site.register(User, CustomUserAdmin)