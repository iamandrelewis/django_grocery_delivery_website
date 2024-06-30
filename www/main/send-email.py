import django
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError

def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Email verification code: {0}'.format(user.email_token)
    email_body = render_to_string('main/emails/acivate-email.html',{
        'user': user,
        'domain':current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.id)),
    })

#EmailMessage()

def send_reset_password(user,request):
    current_site = get_current_site(request)
    email_subject = ""
    email_body = render_to_string('main/emails/reset-password.html',{
        'user':user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes())
    })

