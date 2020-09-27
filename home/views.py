from django.shortcuts import render
from .models import Realtor
from django.views.generic import DetailView

# Create your views here.
def index(request):
    realtors = Realtor.objects.order_by('-hire_date')
    context = {
        'realtors': realtors,
       
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

