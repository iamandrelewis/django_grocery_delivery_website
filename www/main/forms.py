from typing import Any, Dict
from django import forms
from django.utils.translation import gettext_lazy
from django.contrib.auth import get_user_model
from users.models import CustomUser
from . import models as m

class LoginForm(forms.Form):
    email = forms.CharField(label='', widget=forms.TextInput(attrs={
    'type':'email',
    'placeholder':'Email Address',
    'class':'form-field login email-input g8-input',
    'id':'email',
    }))
    password = forms.CharField(label='',widget=forms.TextInput(attrs={
    'type':'password',
    'placeholder' :'Password',
    'class':'form-field login password-input g8-input',
    'id':'password',
    }))

    def clean(self) -> Dict[str, Any]:
        super(LoginForm,self).clean()
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            user = None
            self.add_error('email',forms.ValidationError("Email is not found"))
        if user is not None:
            valid_pass = CustomUser.check_password(user,raw_password=password)
            if not valid_pass:
                self.add_error('password',forms.ValidationError("Password is incorrect"))

        print(self.errors)
        return self.cleaned_data
    

class BusinessCreationForm(forms.ModelForm):
    BUSINESS_CATEGORIES=[('0','What do you do?'),
                         ('Restaurant','Restaurant'),
                         ('Canteen','Canteen'),
                         ('Food Truck', 'Food Truck'),
                         ('Bakery','Bakery'),
                         ('Manufacturer','Manufacturer'),
                         ('Catering Service', 'Catering Service'),
                         ('General: I provide a SERVICE', 'General: I provide a Service'),
                         ('General: I make a PRODUCT', 'General: I make a PRODUCT')
                         ]

    PARISHES = [('0','Parish'),
                ('Saint Andrew','Saint Andrew'),
                ('Kingston','Kingston'),
                ('Saint Catherine','Saint Catherine'),
                ('Clarendon','Clarendon'),
                ('Manchester','Manchester'),
                ('Saint Elizabeth','Saint Elizabeth'),
                ('Westmoreland','Westmoreland'),
                ('Hanover','Hanover'),
                ('Trelawny','Trelawny'),
                ('Saint James','Saint James'),
                ('Saint Ann','Saint Ann'),
                ('Saint Mary','Saint Mary'),
                ('Portland','Portland'),
                ('Saint Thomas','Saint Thomas')
                ]

    business_name = forms.CharField(required=True,label='',widget=forms.TextInput(attrs={
        'type':'text',
        'placeholder':'Business Name',
        'class':'g8-input',
    }))
    business_category = forms.ChoiceField(required=True,label='',widget=forms.Select(attrs={
        'class': 'g8-select',
    }),choices=BUSINESS_CATEGORIES)

    address_line1 = forms.CharField(required=True,label='',widget=forms.TextInput(attrs={
        'type':'text',
        'placeholder':'Street',
        'class':'g8-input',
    }))
    address_line2 = forms.CharField(required=True,label='',widget=forms.TextInput(attrs={
        'type':'text',
        'placeholder':'City',
        'class':'g8-input',
    }))
    parish = forms.ChoiceField(label='',widget=forms.Select(attrs={
        'class': 'g8-select',        
    }),choices=PARISHES)
    class Meta:
        model = m.UserBusiness
        fields = ["business_name","business_category","address_line1","address_line2","parish"]

    def clean_business_category(self,*args,**kwargs):
        business_category = self.cleaned_data.get('business_category')
        if business_category == '0':
            raise forms.ValidationError("Select a business category")
        else:
            print(business_category)
        return business_category
        
    def clean_parish(self,*args,**kwargs):
        parish = self.cleaned_data.get('parish')
        if parish == '0':
            raise forms.ValidationError("Select a parish")
        else:
            print(parish)
        return parish
    
class AddressCreationForm(forms.ModelForm):
    PARISHES = [('0','Parish'),
                ('Saint Andrew','Saint Andrew'),
                ('Kingston','Kingston'),
                ('Saint Catherine','Saint Catherine'),
                ('Clarendon','Clarendon'),
                ('Manchester','Manchester'),
                ('Saint Elizabeth','Saint Elizabeth'),
                ('Westmoreland','Westmoreland'),
                ('Hanover','Hanover'),
                ('Trelawny','Trelawny'),
                ('Saint James','Saint James'),
                ('Saint Ann','Saint Ann'),
                ('Saint Mary','Saint Mary'),
                ('Portland','Portland'),
                ('Saint Thomas','Saint Thomas')
                ]

    address_line1 = forms.CharField(required=True,label='',widget=forms.TextInput(attrs={
        'type':'text',
        'placeholder':'Street',
        'class':'g8-input',
    }))
    address_line2 = forms.CharField(required=True,label='',widget=forms.TextInput(attrs={
        'type':'text',
        'placeholder':'City',
        'class':'g8-input',
    }))
    parish = forms.ChoiceField(label='',widget=forms.Select(attrs={
        'class': 'g8-select',        
    }),choices=PARISHES)
    class Meta:
        model = m.UserAddress
        fields = ["address_line1","address_line2","parish"]
        
    def clean_parish(self,*args,**kwargs):
        parish = self.cleaned_data.get('parish')
        if parish == '0':
            raise forms.ValidationError("Select a parish")
        else:
            print(parish)
        return parish
    


