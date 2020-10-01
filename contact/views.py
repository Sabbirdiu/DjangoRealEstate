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

# def contact(request):

#     return render(request,'contact-us.html')    

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

    # Send email
    # send_mail(
    #   'Property Listing Inquiry',
    #   'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
    #   'traversy.brad@gmail.com',
    #   [realtor_email, 'techguyinfo@gmail.com'],
    #   fail_silently=False
    # )

    messages.success(request, 'Your request has been submitted')
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
    if request.method == 'POST':
      auth.logout(request)
      messages.success(request, 'You are now logged out')
      return redirect('home')        
def myaccount(request):
    return render(request,'my-account.html')            
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # p_form = ProfileUpdateForm(request.POST,
        #                            request.FILES,
        #                            instance=request.user.profile)
        if u_form.is_valid().is_valid():
            u_form.save()
           
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        # p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        # 'p_form': p_form
    }
    return render(request,'my-account.html',context)


def edit_profile(request):
    # context = {}
    # check = register_table.objects.filter(user__id=request.user.id)
    # if len(check)>0:
    #     data = register_table.objects.get(user__id=request.user.id)
    #     context["data"]=data    
      if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']

        user = User.objects.get(id=request.user.id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.save()

        context["status"] = "Changes Saved Successfully"
      return render(request,"my-account.html",context)
