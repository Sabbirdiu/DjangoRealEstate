from django.shortcuts import render
from .models import Realtor,Listing
from django.views.generic import DetailView

# Create your views here.
def index(request):
    featured = Listing.objects.filter(featured=True)
    latest = Listing.objects.order_by('-list_date')[0:6]
    realtors = Realtor.objects.order_by('-hire_date')
    products_slider = Listing.objects.all().order_by('-id')[:2]
    context = {
        'realtors': realtors,
        'object_list':featured,
        'latest':latest,
        'products_slider':products_slider
       
    }
     
    return render(request, 'index.html', context)
def agents(request):
    realtors = Realtor.objects.order_by('-hire_date')
    context = {
        'realtors': realtors,   
    } 
    return render(request, 'agents.html', context)
class AgentDetailView(DetailView):
    model = Realtor  
    template_name = 'agent-details.html'        

