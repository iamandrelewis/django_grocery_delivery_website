from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from main.models import UserReferrals,UserAddress
initial_referer = str()
def account_settings(request,uid=None):
    global initial_referer 
    try:
        initial_referer = request.META['HTTP_REFERER']
    except:
        initial_referer = reverse('homepage')
    return render(request,'users/account-settings.html',{'back_link': initial_referer})
def account_address(request,uid=None):
    global initial_referer 
    address = UserAddress.objects.filter(user=request.user)
    return render(request,'users/account-settings-address.html',{'back_link': initial_referer,
        'addresses':address
    })
def account_subscriptions(request,uid=None):
    global initial_referer
    return render(request,'users/account-settings-sub-payments.html',{'back_link': initial_referer})
def account_security(request,uid=None):
    global initial_referer
    return render(request,'users/account-settings-security-privacy.html',{'back_link': initial_referer})
def account_referrals(request,uid=None):
    global initial_referer
    current_site = get_current_site(request)
    referees = UserReferrals.objects.filter(referer = request.user)
    return render(request,'users/account-referrals.html',{
        'domain': current_site,
        'back_link': initial_referer,
        'referers':referees,
        'credit_limit':request.user.userstorecredit_set.first().creditLimit
    })