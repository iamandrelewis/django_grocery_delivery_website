from django.contrib import admin

# Register your models here.
from .models import UserAddress,UserReferrals

admin.site.register(UserAddress)
admin.site.register(UserReferrals)