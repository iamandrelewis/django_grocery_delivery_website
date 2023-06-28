from django.urls import path
from . import views as v

urlpatterns = [
    path('terms',v.terms,name='terms'),
    path('privacy-policy',v.privacy,name='privacy-policy'),
    path('refunds',v.refund,name='refund'),
    path('faqs',v.faqs,name='faqs'),
    path('make-a-suggestion',v.feedback,name='feedback'),
]