from django.shortcuts import render
from .models import Realtor

# Create your views here.
def index(request):
    realtors = Realtor.objects.order_by('-hire_date')
    context = {
        'realtors': realtors,
       
    }
    

   
    return render(request, 'index.html', context)