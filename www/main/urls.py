from django.urls import path
from . import views as v

urlpatterns = [
    path('',v.home,name='homepage'),
    path('signin',v.sigin,name='signin'),
    path('signup',v.signup,name='signup'),
    path('signup/a/<str:ref_code>',v.signup_referral,name='signup-referral'),
    path('logout/',v.signout,name='signout'),
    path('recovery',v.recovery,name='account-recovery'),
    path('recovery/email',v.recover_email,name='email-recovery'),
    path('checkout-aisle',v.checkout_aisle,name='checkout-aisle'),
    path('checkout',v.checkout,name='checkout'),
    path('premium',v.premium,name='premium'),
    path('the-birthday-club',v.birthday_club,name='birthday-club'),
    path('store-credit',v.store_credit,name='store-credit'),
    path('activate/<uidb64>/<token>',v.activate_user,name='activate')
]