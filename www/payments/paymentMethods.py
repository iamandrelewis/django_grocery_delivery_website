import stripe

stripe.api_key='sk_test_51J3aWELy14BTTUlmwwxJC8LQFP2SeVoo4k6QmDmELBRxEwX7FBDBkPAHAfrmLZ3r1WN3dMKe9LvbGx3EVk8JogoR00qXR96WMC'

def create(**kwargs):
        try:
            if(kwargs['type']=='card'):
                stripe.PaymentMethod.create(
                    type=f"{kwargs[type]}",
                    card={
                        "number": f"{kwargs['card_number']}",
                        "exp_month": kwargs['exp_month'],
                        "exp_year": kwargs['exp_year'],
                        "cvc": f"{kwargs['cvc']}",
                    },
                    billing_details={
                       "name": f"{kwargs['first_name']} {kwargs['last_name']}",
                       "address": {
                            "city": f"{kwargs['city']}",
                            "country":f"{kwargs['country']}",
                            "line1":f"{kwargs['line1']}",
                            "line2":f"{kwargs['line2']}"
                       }
                    },
                )
            elif(kwargs["type"] =='cashapp'):
                 pass
        except: 
            return 'Something went wrong! :('



def attach(cust_id,card_number,exp_month,exp_year,cvc,line1,line2,city,country):
    try:
        return stripe.PaymentMethod.attach(
            create(type='card',card_number=card_number,exp_month=exp_month,exp_year=exp_year,cvc=cvc,line1=line1,line2=line2,city=city,country=country),
            customer=f"{cust_id}",
        )
    except:
        return 'Something went wrong! :('

