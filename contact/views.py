from django.shortcuts import render
from django.http import HttpResponse
from home.models import Listing,Realtor
from .models import About,Partnars
# Create your views here.
def about(request):
    service_slider = Listing.objects.all().order_by('-id')[:4]
    realtors = Realtor.objects.order_by('-hire_date')[0:6]
    about = About.objects.all()
    partnar = Partnars.objects.all().order_by('-id')[:5]
    context = {
        'service_slider':service_slider,
        'realtors': realtors,
        'about':about,
        'partnar':partnar
       
       
    }
    return render(request,'about-us.html',context)

def contact(request):
    return render(request,'contact-us.html')    

def log_reg(request):
    return render(request,'login-register.html')        
def myaccount(request):
    return render(request,'my-account.html')            