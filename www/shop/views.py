from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from main import models as m
from orders.models import Order,OrderItem
from .models import ProductGrade
import datetime
import json
from django.http import JsonResponse,HttpResponseBadRequest

# Create your views here.
@login_required(login_url='signin')
def shop(request):
        if 'order_id' not in request.session:
            try:
                order = Order.objects.get(fulfilment_status='Unfulfilled',payment_status='Pending',user=request.user,order_status='Draft')
            except Order.DoesNotExist:
                order = Order.objects.create(user=request.user)
                request.session['order_id'] = order.pk
        else:
            try:
                order = Order.objects.get(pk = request.session['order_id'])
            except Order.DoesNotExist:
                order = Order.objects.create(user=request.user)
                request.session['order_id'] = order.pk

        items = order.orderitem_set.all()
        return render(request,'shop/main.html',{'items':items})

@login_required(login_url='signin')
def green_produce(request):
    return redirect('green_produce-all')

@login_required(login_url='signin')
def green_produce_all(request):
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

    items = order.orderitem_set.all()
    products = ProductGrade.objects.filter(grade__exact='A', product__product__subcategory__category__name__exact="Green Produce")
    return render(request,'green_produce/main.html',{
        "products":products,
        "items":items,
        "order":order
         })

@login_required(login_url='signin')
def green_produce_fruits(request):
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

    items = order.orderitem_set.all()
    products = ProductGrade.objects.filter(grade__exact='A', product__product__subcategory__name__exact="Fruits")
    return render(request,'green_produce/fruits/main.html',{
        "products":products,
        "items":items,
        "order":order
         })

@login_required(login_url='signin')
def green_produce_vegetables(request):
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

    items = order.orderitem_set.all()
        
    products = ProductGrade.objects.filter(grade__exact='A', product__product__subcategory__name__exact="Vegetables")

    return render(request,'green_produce/vegetables/main.html',{
        "products":products,
        "items":items,
        "order":order
         })

@login_required(login_url='signin')
def green_produce_herbs_spices(request):
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

    items = order.orderitem_set.all()
    products = ProductGrade.objects.filter(grade__exact='A', product__product__subcategory__name__exact="Herbs & Spices")

    return render(request,'green_produce/herbs-spices/main.html',{
        "products":products,
        "items":items,
        "order":order
         })

@login_required(login_url='signin')
def green_produce_tubers_provisions(request):
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

    items = order.orderitem_set.all()
    products = ProductGrade.objects.filter(grade__exact='A', product__product__subcategory__name__exact="Tubers & Provisions")

    return render(request,'green_produce/tubers-provisions/main.html',{
        "products":products,
        "items":items,
        "order":order
         })

@login_required(login_url='signin')
def green_produce_nuts_grains(request):
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

    items = order.orderitem_set.all()
    products = ProductGrade.objects.filter(grade__exact='A', product__product__subcategory__name__exact="Nuts & Grains")

    return render(request,'green_produce/nuts-grains/main.html',{
        "products":products,
        "items":items,
        "order":order
         })

@login_required(login_url='signin')
def meats(request):
    return redirect('meats-all')

@login_required(login_url='signin')
def meats_all(request):
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

    items = order.orderitem_set.all()
    products = ProductGrade.objects.filter(grade__exact='A', product__product__subcategory__category__name__exact="Meats")

    return render(request,'meats/main.html',{
        "products":products,
        "items":items,
        "order":order
         })

@login_required(login_url='signin')
def meats_poultry(request):
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

    items = order.orderitem_set.all()
    products = ProductGrade.objects.filter(grade__exact='A', product__product__subcategory__name__exact="Poultry")

    return render(request,'meats/poultry/main.html',{
        "products":products,
        "items":items,
        "order":order
         })

@login_required(login_url='signin')
def meats_lean(request):
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

    items = order.orderitem_set.all()
    products = ProductGrade.objects.filter(grade__exact='A', product__product__subcategory__name__exact="Lean Meats")

    return render(request,'meats/lean/main.html',{
        "products":products,
        "items":items,
        "order":order
         })


@login_required(login_url='signin')
def meats_fish_seafood(request):
    """
    """
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

    items = order.orderitem_set.all()
    products = ProductGrade.objects.filter(grade__exact='A', product__product__subcategory__name__exact="Fish & Seafood")
    return render(request,'meats/fish-seafood/main.html',{
        "products":products,
        "items":items,
        "order":order
         })


@login_required(login_url='signin')
def meats_deli(request):
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

    items = order.orderitem_set.all()
    products = ProductGrade.objects.filter(grade__exact='A', product__product__subcategory__name__exact="Deli")

    return render(request,'meats/deli/main.html',{
        "products":products,
        "items":items,
        "order":order
         })

@login_required(login_url='signin')
def deals(request):
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

    return render(request,'shop/deals/main.html')

@login_required(login_url='signin')
def buy_it_again(request):
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

    return render(request,'shop/buy_it_again/main.html')

@login_required(login_url='signin')
def product_details(request, details=None,pk=None):
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
        product = ProductGrade.objects.get(product__product_id=details,product_id=pk)
        try:
            orderitem = order.orderitem_set.get(product_grade__product_id=pk)
            print(orderitem)

        except:
            orderitem = None
            print(orderitem)
    except ProductGrade.DoesNotExist:
        return HttpResponseBadRequest(request)
    return render(request,'shop/product-details.html',{
        'product':product,
        'order': orderitem
    })


def update_cart(request):
    """
    """
    data = json.loads(request.body)
    productID = data['productID']
    action = data['action']
    print("productID: {0} | Action: {1}".format(productID,action))
    if(action == 'add'):
        try:
            item = OrderItem.objects.get(order_id=request.session['order_id'],product_grade_id=productID)
            try:
                item.quantity = int(item.quantity) + 1
            except:
                item.quantity = float(item.quantity) + 1
            item.save(update_fields=['quantity'])
        except:
            print(ProductGrade.objects.get(pk=productID))
            OrderItem.objects.create(order_id=request.session['order_id'],product_grade_id=productID,quantity='1')
    elif(action == 'remove'):
        try:
            item = OrderItem.objects.get(order_id=request.session['order_id'],product_grade_id=productID)
            item.delete()
        except:
            return JsonResponse("Cart was not updated",safe=False)
    elif(action == 'getCartCount'):
        try:
            items = OrderItem.objects.filter(order_id=request.session['order_id'])
            return JsonResponse(f'{items.count()}',safe=False)
        except:
            return JsonResponse('0',safe=False)
    


    return JsonResponse("Cart was updated",safe=False)