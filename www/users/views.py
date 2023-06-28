from django.shortcuts import render,redirect

def account_settings(request,uid=None):
    return render(request,'users/account-settings.html')
def account_address(request,uid=None):
    return render(request,'users/account-settings-address.html')
def account_subscriptions(request,uid=None):
    return render(request,'users/account-settings-sub-payments.html')
def account_security(request,uid=None):
    return render(request,'users/account-settings-security-privacy.html')
def account_referrals(request,uid=None):
    return render(request,'users/account-referrals.html')