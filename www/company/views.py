from django.shortcuts import render

# Create your views here.
def about_us(request):
    return render(request,'company/about-us.html')

def careers(request):
    return render(request,'company/careers.html')

def investors(request):
    return render(request,'company/investors.html')

def how_it_works(request):
    return render(request,'company/how-it-works.html')