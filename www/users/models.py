import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from .managers import CustomUserManager
from . import utils as _u

class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(_("id"),primary_key=True,default=uuid.uuid4)
    email = models.EmailField(_("email address"), unique=True)
    first_name= models.CharField(_("first name"),max_length=200)
    last_name = models.CharField(_("last name"),max_length=200)
    date_of_birth = models.DateField(_("date of birth"), auto_now=True) #null=True,default=None,blank=True)
    phone_number = models.CharField(_("phone number"),max_length=20)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    """email_is_validated  = models.BooleanField(_("email validation status"),default=False)
    phone_is_validated = models.BooleanField(_("phone validation status"),default=False)
    email_token = models.CharField(max_length=6,default=_u.generate_email_verification_token,unique=True)
    email_token_timestamp = models.DateTimeField(auto_now_add=True)
    email_token_is_expired = models.BooleanField(default=False)
    sms_token = models.CharField(max_length=6,default=_u.generate_sms_verification_token,unique=True)
    sms_token_timestamp = models.DateTimeField(auto_now_add=True)
    email_token_is_expired = models.BooleanField(default=False)
    gender = models.CharField(max_length=128,null=True,default=None blank=True)
    ref_code = models.CharField(max_length=12,default=_u.generate_ref_code)"""

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []#first_name,last_name]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    """def get_referral_url(self):
        return reverse('signup-referral',kwargs={"ref_code": self.ref_code})"""
    
    """def generate_email_verification_token():
        return _u.generate_email_verification_token()
    """

    """def generate_sms_verification_token():
        return _u.generate_sms_verification_token()
    """
    """def check_email_verification_token():
        one_day_in_seconds = 86400
        time_passed_in_seconds = self.email_token_timestamp - datetime.now
        if time_passed_in_second.total_seconds > one_day_in_seconds:
            self.email_token_is_expired = True
            self.save(update_fields=['email_token_is_expired'])
    """