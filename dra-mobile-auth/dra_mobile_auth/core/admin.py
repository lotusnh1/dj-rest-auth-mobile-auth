from django.contrib import admin

from .models import Otp

class OtpAdmin(admin.ModelAdmin):
    list_display = ["code", "phonenumber"]
    search_fields = ['code', 'phonenumber']


admin.site.register(Otp,OtpAdmin)
