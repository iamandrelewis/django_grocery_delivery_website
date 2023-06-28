from django.urls import path
from . import views as v
urlpatterns = [
    path('settings',v.account_settings,name='account-settings'),
    path('addresses',v.account_address,name='account-address'),
    path('subscriptions',v.account_subscriptions,name='account-subscriptions'),
    path('security',v.account_security,name='account-security'),
    path('referrals',v.account_referrals,name='account-referrals'),
]