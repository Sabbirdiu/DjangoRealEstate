from django.shortcuts import render,redirect
# from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from home.models import Listing,Realtor
from .models import About,Partnars,Contact
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserUpdateForm
from django.contrib.auth.decorators import login_required
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
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    subject = request.POST['subject']
    message = request.POST['message']
    user_id = request.POST['user_id']
    

    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter( user_id=user_id)
      # if has_contacted:
      #   messages.error(request, 'You have already made an inquiry for this listing')
      #   return redirect('contact')

    contact = Contact(name=name, email=email, phone=phone,subject='subject', message=message, user_id=user_id )

    contact.save()

 

    messages.success(request, 'Your reqmessage  has been submitted')
    return redirect('contact')

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
      return redirect('account')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'login.html') 
   
    
def logout(request):
    if request.method == 'POST':
      auth.logout(request)
      messages.success(request, 'You are now logged out')
      return redirect('login')        
def myaccount(request):
    return render(request,'my-account.html')            
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
                               
        if  u_form.is_valid():
            u_form.save()
           
            messages.success(request, f'Your account has been updated!')
            return redirect('account')

    else:
        u_form = UserUpdateForm(instance=request.user)
      

    context = {
        'u_form': u_form,
       
    }
    return render(request,'my-account.html',context)


