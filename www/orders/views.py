from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='signin')
def orders(request):
    return render(request,'orders/main.html')

@login_required(login_url='signin')
def activity(request):
    return render(request,'orders/order-activity.html')

@login_required(login_url='signin')
def recurring(request):
    return render(request,'orders/recurring-orders.html')

@login_required(login_url='signin')
def pending(request):
    return render(request,'orders/pending-orders.html')

def refunds(request):
    pass

@login_required(login_url='signin')
def activity_details(request):
    return render(request,'orders/order-activity-detail.html')

@login_required(login_url='signin')
def recurring_details(request):
    return render(request,'orders/order-recurring-detail.html')

@login_required(login_url='signin')
def recurring_add(request):
    return render(request,'orders/order-recurring-add.html')