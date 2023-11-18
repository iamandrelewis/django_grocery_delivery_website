from django.shortcuts import render
import json
from . import paymentMethods
from . import models as m
# Create your views here.

def api(request):
    """
    """
    try:
        data = json.loads(request.body)
        if(data['action'] =='add-method'):
            try:
                response = paymentMethods.attach(request.user.stripe_acc_id,data['card_number'],data['exp_month'],data['exp_year'],data['cvc'],data['line1'],data['line2'],data['city'],data['country'])
                print(response)
            except:
                print('Something went wrong')
        elif(data['action'] == 'create-intent'):
            pass
    except:
        print('payment')
    

