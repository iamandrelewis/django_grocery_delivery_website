from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from users.forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import BusinessCreationForm,LoginForm
from shop.models import ProductGrade,ProductVarietie,Product,ProductSubCategorie,ProductCategorie
from orders.models import Order
from . import models as m
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
from users.models import CustomUser 

"""def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Email verification code: {0}'.format(user.email_token)
    email_body = render_to_string('main/acivate-email.html',{
        'user': user,
        'domain':current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.id)),
    })
"""
def home(request):
    if request.POST:
        print(request.POST)
    if request.user.is_authenticated:
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
        request.user.check_email_verification_token()
        try:
            m.UserAddress.objects.get(user=request.user,default_status=True)
            m.UserBusiness.objects.get(user=request.user)
        except:
            if request.user.is_superuser:
                a = m.UserAddress.objects.create(user=request.user,address_line1="69 Coolshade Drive",address_line2='Kingston 19',parish='Saint Andrew',default_status=True)
                m.UserBusiness.objects.create(user=request.user,business_name='GR8 Grocers Meats and More Limited',business_category='G',business_address=a)
            return redirect('signup')
        address = m.UserAddress.objects.get(default_status=True,user = request.user)
        business = m.UserBusiness.objects.get(user = request.user)
        products = ProductGrade.objects.filter(grade="A")
        print(ProductCategorie.objects.get(pk=ProductSubCategorie.objects.get(pk=Product.objects.get(pk=ProductVarietie.objects.get(pk=products[1].product_id).product_id).subcategory_id).category_id))
        context = {
            'business': business,
            'products': products
        }
        return render(request,'main/home.html', context)
    return render(request,'main/home.html')

def sigin(request):
    """
    Accepts requests and renders the signin form, 
    allowing users to be autheniticated and logged in,
    if credentials are entered correctly and users weren't previously,
    otherwise, they'll either be prompted of an error
    or redirected to the homepage
    """
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        if form.is_valid():
            user = authenticate(request, username=email,password=password)
            if user is not None:
                login(request, user)
                try: 
                    assert(request.GET['next'] != None)
                    return redirect(request.GET['next'])
                except:
                    return redirect('homepage')
        return render(request,'registration/login.html',{"form":form})
    else:           
        if request.user.is_authenticated:
            try: 
                assert(request.GET['next'] != None)
                return redirect(request.GET['next'])
            except:
                return redirect('homepage')
    return render(request,'registration/login.html',{"form":form})

def signup_referral(request,ref_code=None):
    if ref_code != None:
        request.session['referer_code'] = ref_code
    return redirect('signup')

def signup(request):
    """
    """
    if not request.user.is_authenticated:
        form = CustomUserCreationForm(request.POST or None)
        if request.method == "POST":
            print(request.POST)
            if form.is_valid():
                form.save()
                user = authenticate(request, username=request.POST['email'],password=request.POST['password1'])
                print(user)
                if user is not None:
                    login(request, user)
                return redirect('signup')
            else:
                print(form.error_messages)
        return render(request,'registration/signup.html',{"form":form})
    else:
        try:
            m.UserAddress.objects.get(user=request.user,default_status=True)
            m.UserBusiness.objects.get(user=request.user)
        except:

            if 'referer_code' in request.session:
                referer = CustomUser.objects.get(ref_code=request.session.get('referer_code'))
                referral = m.UserReferrals.objects.create(referee=request.user,referer=referer)
                print(referral)
                del request.session['referer_code']
            form = BusinessCreationForm(request.POST or None)
            if request.method == "POST":
                if form.is_valid():
                    print(request.POST)
                    address,created = m.UserAddress.objects.get_or_create(user = request.user, address_line1 = request.POST['address_line1'],address_line2 = request.POST['address_line2'],parish = request.POST['parish'],default_status = True)
                    business = form.save(commit=False)
                    business.user = request.user
                    business.business_address = address 
                    business.save()
                    return redirect('homepage')
                else:
                    print(form.errors)
                    return redirect('signup')
            return render(request,'registration/add_business.html',{"form":form})
        return redirect('homepage')  

def recover_email(request):
    return render(request,'registration/email-lookup.html')

def recovery(request):
    return render(request,'registration/account-recovery.html')

def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('homepage')
    return redirect('signin')

@login_required(login_url='signin')
def checkout_aisle(request):
    return render(request,'main/checkout-aisle.html')

@login_required(login_url='signin')
def checkout(request):
    return render(request,'main/checkout.html')

def premium(request):
    return render(request,'main/premium.html')

def birthday_club(request):
    return render(request,'main/the-birthday-club.html')

def activate_user(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except Exception as e:
        user = None
    if user and user.email_token == token:
        user.email_is_validated = True
        user.save()
        return render(request,'main/activate-success.html',{'e':user})
    return render(request,'main/activate-failiure.html',{'e':uid})

def store_credit(request):
    current_site = get_current_site(request)
    return render(request,'main/activate-email.html',{'domain':current_site,
        'uid': urlsafe_base64_encode(force_bytes(request.user.id))})