from django.contrib import admin

# Register your models here.
from .models import UserAddress,UserReferrals,UserStoreCredit,UserMembership

admin.site.register(UserAddress)
admin.site.register(UserReferrals)
admin.site.register(UserStoreCredit)
admin.site.register(UserMembership)