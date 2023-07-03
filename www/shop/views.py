from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from main import models as m

# Create your views here.
@login_required(login_url='signin')
def shop(request):
    return render(request,'shop/main.html')
@login_required(login_url='signin')
def green_produce(request):
    return redirect('green_produce-all')

@login_required(login_url='signin')
def green_produce_all(request):
    return render(request,'green_produce/main.html')

@login_required(login_url='signin')
def green_produce_fruits(request):
    return render(request,'green_produce/fruits/main.html')

@login_required(login_url='signin')
def green_produce_vegetables(request):
    return render(request,'green_produce/vegetables/main.html')

@login_required(login_url='signin')
def green_produce_herbs_spices(request):
    return render(request,'green_produce/herbs-spices/main.html')

@login_required(login_url='signin')
def green_produce_tubers_provisions(request):
    return render(request,'green_produce/tubers-provisions/main.html')

@login_required(login_url='signin')
def green_produce_nuts_grains(request):
    return render(request,'green_produce/nuts-grains/main.html')

@login_required(login_url='signin')
def meats(request):
    return redirect('meats-all')

@login_required(login_url='signin')
def meats_all(request):
    return render(request,'meats/main.html')

@login_required(login_url='signin')
def meats_poultry(request):
    return render(request,'meats/poultry/main.html')

@login_required(login_url='signin')
def meats_lean(request):
    return render(request,'meats/lean/main.html')


@login_required(login_url='signin')
def meats_fish_seafood(request):
    return render(request,'meats/fish-seafood/main.html')


@login_required(login_url='signin')
def meats_deli(request):
    return render(request,'meats/deli/main.html')

@login_required(login_url='signin')
def deals(request):
    return render(request,'shop/deals/main.html')

@login_required(login_url='signin')
def buy_it_again(request):
    return render(request,'shop/buy_it_again/main.html')

@login_required(login_url='signin')
def product_details(request):
    return render(request,'shop/product-details.html')


