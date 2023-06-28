from django.shortcuts import render

# Create your views here.
def terms(request):
    return render(request,'legal/terms.html')

def privacy(request):
    return render(request,'legal/privacy-policy.html')

def faqs(request):
    return render(request,'legal/faqs.html')

def feedback(request):
    return render(request,'legal/feedback.html')

def refund(request):
    return render(request,'legal/refund-policy.html')