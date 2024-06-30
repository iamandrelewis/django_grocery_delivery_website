from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse,HttpResponseBadRequest
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
from .models import Order, RecurringOrder
from main import models as m

# Create your views here.
@login_required(login_url='signin')
def orders(request):
    if 'order_id' not in request.session:
        try:
            order = Order.objects.get(fulfilment_status='Unfulfilled',payment_status='Pending',user=request.user,order_status='Draft')
        except Order.DoesNotExist:
            order = Order.objects.create(user=request.user)
        request.session['order_id'] = order.pk
    else:
        try:
            order = Order.objects.get(pk=request.session['order_id'])
        except Order.DoesNotExist:
            order = Order.objects.create(user=request.user)
            request.session['order_id'] = order.pk
    try:
        name = m.UserBusiness.objects.get(user=request.user).business_name  
    except:
        name = f'{request.user.first_name} {request.user.last_name}'
    return render(request,'orders/main.html',{'order':order,'name':name})

@login_required(login_url='signin')
def activity(request):
    try:
        orders = Order.objects.filter(user=request.user)
    except Exception as e:
        orders = None
    try:
        name = m.UserBusiness.objects.get(user=request.user).business_name  
    except:
        name = f'{request.user.first_name} {request.user.last_name}'
    return render(request,'orders/order-activity.html',{'orders':orders,'name':name})

@login_required(login_url='signin')
def recurring(request):
    try:
        name = m.UserBusiness.objects.get(user=request.user).business_name  
    except:
        name = f'{request.user.first_name} {request.user.last_name}'
    return render(request,'orders/recurring-orders.html',{'name':name})

@login_required(login_url='signin')
def pending(request):
    try:
        name = m.UserBusiness.objects.get(user=request.user).business_name  
    except:
        name = f'{request.user.first_name} {request.user.last_name}'
    return render(request,'orders/pending-orders.html',{
        'name':name
    })

def refunds(request):
    pass

@login_required(login_url='signin')
def activity_details(request,refidb64):
    try:
        ref_id = force_str(urlsafe_base64_decode(refidb64))
        order = Order.objects.get(reference_id=ref_id)
        items = order.orderitem_set.all()
    except Exception as e:
        order = None
    try:
        name = m.UserBusiness.objects.get(user=request.user).business_name  
    except:
        name = f'{request.user.first_name} {request.user.last_name}'
    return render(request,'orders/order-activity-detail.html',{'order':order, 'items':items,'name':name})

@login_required(login_url='signin')
def recurring_details(request):#,refidb64):
    """try:
        ref_id = force_str(urlsafe_base64_decode(refidb64))
        order = RecurringOrder.objects.get(order__reference_id=ref_id)
    except Exception as e:
        order = None"""
    try:
        name = m.UserBusiness.objects.get(user=request.user).business_name  
    except:
        name = f'{request.user.first_name} {request.user.last_name}'
    return render(request,'orders/order-recurring-detail.html',{
        'name':name
    })

@login_required(login_url='signin')
def recurring_add(request):
    if 'recur_order_id' not in request.session:
        recurring_order = RecurringOrder.objects.create(order__user=request.user)
    try:
        name = m.UserBusiness.objects.get(user=request.user).business_name  
    except:
        name = f'{request.user.first_name} {request.user.last_name}'
    return render(request,'orders/order-recurring-add.html',{
        'name': name
    })

@login_required(login_url='signin')
def delivery_map(request):
    try:
        name = m.UserBusiness.objects.get(user=request.user).business_name  
    except:
        name = f'{request.user.first_name} {request.user.last_name}'
    return render(request,'orders/reports.html',{
        'name': name
    })

@login_required(login_url='signin')
def recurring_update(request):
    data = json.loads(request.body)

    return JsonResponse("Order was updated",safe=False)