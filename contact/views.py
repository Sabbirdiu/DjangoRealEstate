from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    return render(request,'about-us.html')

def contact(request):
    return render(request,'contact-us.html')    

def log_reg(request):
    return render(request,'login-register.html')        
def myaccount(request):
    return render(request,'my-account.html')            