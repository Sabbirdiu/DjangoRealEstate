from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import Listing,Realtor
from .models import About,Partnars
from django.contrib import messages, auth
from django.contrib.auth.models import User

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

def register(request):
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
      # Check username
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is taken')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'That email is being used')
          return redirect('register')
        else:
          # Looks good
          user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
          # Login after register
          # auth.login(request, user)
          # messages.success(request, 'You are now logged in')
          # return redirect('index')
          user.save()
          messages.success(request, 'You are now registered and can log in')
          return redirect('login')
    else:
      messages.error(request, 'Passwords do not match')
      return redirect('register')
  else:
    return render(request, 'register.html')
def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('dashboard')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'login.html') 
def dashboard(request):
    return render(request,'dashboard.html')      
def log_reg(request):
    return render(request,'login-register.html')      
def logout(request):
    return render(request,'index')        
def myaccount(request):
    return render(request,'my-account.html')            