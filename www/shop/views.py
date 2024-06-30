from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from main import models as m
from orders.models import Order,OrderItem
from .models import ProductGrade,ProductDeal
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
        try:
            name = m.UserBusiness.objects.get(user=request.user).business_name  
        except:
            name = f'{request.user.first_name} {request.user.last_name}'
        return render(request,'shop/main.html',{'items':items, "name": name})

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
    productwall = list()
    for item in items:
        for product in products:
            if product == item.product_grade:
                productwall.append(f"""
            <div class="product_card-container" style="position: relative;">
                <a href="" style="display: block; width: 100%; height: 100%; position: absolute;"></a>
                <div class="product-img">
                    <span></span>
                    <div class="product-add">
                        <div data-product="{product.id}" data-action="add" class="product_add-btn" style="background-color: var(--grey2); border: 1px solid rgb(232,233,235); display: flex; align-items: center;">
                            <input type="text" style="width: 32px; background-color: transparent; outline: none; border: 1px solid transparent; font-size: 14.5px; color: white; font-weight: 600; z-index: 99;" value="{item.quantity}">
                            <span style="font-size: 14px; margin-left: 6px;">{product.unit.unit_abbr}</span>
                        </div>
                    </div>
                </div>
                <div class="product-details">
                    <div class="product-title">
                        <div class="product_price-container">
                            <div class="product-price">
                                <p class="dollars" id="product_price-dollars">${product.price.value}</p>
                            </div>
                        </div>  
                        <p class="product_variety">{product.product.name}</p>
                        <p class="product_name">{product.product.product.name}</p>
                        <p class="product_unit">per {product.unit.unit} ({product.unit.unit_abbr}.)</p> 
                    </div>
                </div>
            </div>
        """)
        else:
            productwall.append(f"""
                <div class="product_card-container" style="position: relative;">
                <a href="url 'product-details' {product.product.product.id} {product.product.id} " style="display: block; width: 100%; height: 100%; position: absolute;"></a>
                <div class="product-img">
                    <span></span>
                    <div class="product-add">
                        <button data-product="{product.id}" data-action="add" class="product_add-btn update-cart">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="#FFFFFF" xmlns="http://www.w3.org/2000/svg" size="24" color="systemGrayscale00"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 3.5A1.5 1.5 0 0 1 13.5 5v5.5H19a1.5 1.5 0 0 1 1.493 1.355L20.5 12a1.5 1.5 0 0 1-1.5 1.5h-5.5V19a1.5 1.5 0 0 1-1.355 1.493L12 20.5a1.5 1.5 0 0 1-1.5-1.5v-5.5H5a1.5 1.5 0 0 1-1.493-1.355L3.5 12A1.5 1.5 0 0 1 5 10.5h5.5V5a1.5 1.5 0 0 1 1.355-1.493L12 3.5Z"></path>
                            </svg>
                        </button>
                    </div>
                </div>
                <div class="product-details">
                    <div class="product-title">
                        <div class="product_price-container">
                            <div class="product-price">
                                <p class="dollars" id="product_price-dollars">${product.price.value}</p>
                            </div>
                        </div>  
                        <p class="product_variety">{product.product.name}</p>
                        <p class="product_name">{product.product.product.name}</p>
                        <p class="product_unit">per {product.unit.unit} ({product.unit.unit_abbr}.)</p> 
                    </div>
                </div>
            </div>
        """)
    #print(productwall)
    try:
        name = m.UserBusiness.objects.get(user=request.user).business_name  
    except:
        name = f'{request.user.first_name} {request.user.last_name}'
    return render(request,'green_produce/main.html',{
        "products":products,
        "items":items,
        "order":order,
        "productwall":productwall,
        'name':name
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
    try:
        name = m.UserBusiness.objects.get(user=request.user).business_name  
    except:
        name = f'{request.user.first_name} {request.user.last_name}'
    return render(request,'green_produce/fruits/main.html',{
        "products":products,
        "items":items,
        "order":order,
        "name": name
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
    try:
        name = m.UserBusiness.objects.get(user=request.user).business_name  
    except:
        name = f'{request.user.first_name} {request.user.last_name}'
    return render(request,'green_produce/vegetables/main.html',{
        "products":products,
        "items":items,
        "order":order,
        "name":name
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
    try:
        name = m.UserBusiness.objects.get(user=request.user).business_name  
    except:
        name = f'{request.user.first_name} {request.user.last_name}'
    return render(request,'green_produce/herbs-spices/main.html',{
        "products":products,
        "items":items,
        "order":order,
        "name": name
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
    try:
        name = m.UserBusiness.objects.get(user=request.user).business_name  
    except:
        name = f'{request.user.first_name} {request.user.last_name}'
    return render(request,'green_produce/tubers-provisions/main.html',{
        "products":products,
        "items":items,
        "order":order,
        "name":name
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
    try:
        name = m.UserBusiness.objects.get(user=request.user).business_name  
    except:
        name = f'{request.user.first_name} {request.user.last_name}'

    items = order.orderitem_set.all()
    products = ProductGrade.objects.filter(grade__exact='A', product__product__subcategory__name__exact="Nuts & Grains")

    return render(request,'green_produce/nuts-grains/main.html',{
        "products":products,
        "items":items,
        "order":order,
        "name":name
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
    try:
        name = m.UserBusiness.objects.get(user=request.user).business_name  
    except:
        name = f'{request.user.first_name} {request.user.last_name}'
    return render(request,'meats/main.html',{
        "products":products,
        "items":items,
        "order":order,
        "name": name
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
    try:
        name = m.UserBusiness.objects.get(user=request.user).business_name  
    except:
        name = f'{request.user.first_name} {request.user.last_name}'
    return render(request,'meats/poultry/main.html',{
        "products":products,
        "items":items,
        "order":order,
        "name": name
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
    try:
        name = m.UserBusiness.objects.get(user=request.user).business_name  
    except:
        name = f'{request.user.first_name} {request.user.last_name}'
    items = order.orderitem_set.all()
    products = ProductGrade.objects.filter(grade__exact='A', product__product__subcategory__name__exact="Lean Meats")

    return render(request,'meats/lean/main.html',{
        "products":products,
        "items":items,
        "order":order,
        "name": name
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
    try:
        name = m.UserBusiness.objects.get(user=request.user).business_name  
    except:
        name = f'{request.user.first_name} {request.user.last_name}'
    return render(request,'meats/fish-seafood/main.html',{
        "products":products,
        "items":items,
        "order":order,
        "name": name
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
    try:
        name = m.UserBusiness.objects.get(user=request.user).business_name  
    except:
        name = f'{request.user.first_name} {request.user.last_name}'
    return render(request,'meats/deli/main.html',{
        "products":products,
        "items":items,
        "order":order,
        "name":name
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
    try:
        name = m.UserBusiness.objects.get(user=request.user).business_name  
    except:
        name = f'{request.user.first_name} {request.user.last_name}'
    return render(request,'shop/deals/main.html',{'products':ProductDeal.objects.all(),
                                                  "name":name})

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
    try:
        name = m.UserBusiness.objects.get(user=request.user).business_name  
    except:
        name = f'{request.user.first_name} {request.user.last_name}'
    return render(request,'shop/buy_it_again/main.html',{
        "name":name,
    })

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
        except:
            orderitem = None
        try:
            related_products = ProductGrade.objects.filter(product__product_id=details).exclude(product_id=pk)
        except:
            related_products = None
    except ProductGrade.DoesNotExist:
        return HttpResponseBadRequest(request)
    try:
        name = m.UserBusiness.objects.get(user=request.user).business_name  
    except:
        name = f'{request.user.first_name} {request.user.last_name}'
    return render(request,'shop/product-details.html',{
        'product':product,
        'order': orderitem,
        'related': related_products,
        'name': name
    })


def update_cart(request):
    """
    """
    data = json.loads(request.body)
    productID = data['productID']
    action = data['action']
    if(action == 'add'):
        try:
            item = OrderItem.objects.get(order_id=request.session['order_id'],product_grade_id=productID)
            try:
                item.quantity = int(item.quantity) + 1
            except:
                item.quantity = float(item.quantity) + 1
            item.save(update_fields=['quantity'])
        except:
            order = OrderItem.objects.create(order_id=request.session['order_id'],product_grade_id=productID,quantity='1')
            return JsonResponse(f'{order.pk}',safe=False)
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