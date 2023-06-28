from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=200,label='',widget=forms.TextInput(attrs={
        'placeholder':'First Name',
        'class':'g8-input',
    }))
    last_name = forms.CharField(max_length=200,label='',widget=forms.TextInput(attrs={
        'placeholder': 'Last Name',
        'class':'g8-input',
    }))
    email = forms.EmailField(max_length=254,label='',widget= forms.EmailInput(attrs={
        'placeholder':'Email Address',
        'class':'g8-input',
    }))
    phone = forms.CharField(max_length=20,label='',widget= forms.TextInput(attrs={
        'placeholder':'Phone Number',
        'type': 'tel',
        'class':'g8-input',

    }))
    password1 = forms.CharField(max_length=256,label='',widget=forms.PasswordInput(attrs={
        'placeholder':'Password',
        'class':'g8-input',
    }))
    password2 = forms.CharField(max_length=256,label='',widget=forms.PasswordInput(attrs={
        'placeholder': "Confirm Password",
        'class':'g8-input',
    }))
    class Meta:
        model = CustomUser
        fields = ("first_name","last_name","email","phone","password1","password2")