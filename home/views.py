from django.shortcuts import render,get_object_or_404
from .models import Realtor,Listing
from news.models import Post
from django.views.generic import DetailView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from contact.models import Partnars
# Create your views here.
def index(request):
    featured = Listing.objects.filter(featured=True).order_by('-list_date')[0:6]
    news_featured = Post.objects.filter(featured=True).order_by('-timestamp')[0:6]
    latest = Listing.objects.order_by('-list_date')[0:6]
    realtors = Realtor.objects.order_by('-hire_date')[:6]
    products_slider = Listing.objects.all().order_by('-id')[:2]
    service_slider = Listing.objects.all().order_by('-id')[:4]
    partnar = Partnars.objects.all().order_by('-id')[:5]
    context = {
        'realtors': realtors,
        'object_list':featured,
        'latest':latest,
        'products_slider':products_slider,
        'service_slider':service_slider,
        'news_object_list':news_featured,
        'partnar':partnar
       
    }
     
    return render(request, 'index.html', context)

def listing(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 1)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    featured = Listing.objects.filter(featured=True).order_by('-list_date')[0:3]
    realtors = Realtor.objects.order_by('-hire_date')[:3]
    context = {
        'listings':paged_listings,
        'object_list':featured,
        'realtors':realtors,
    }    
    return render(request, 'properties-list-left-sidebar.html', context)


def listingdetail(request, slug):
  listing = get_object_or_404(Listing, slug=slug)
  featured = Listing.objects.filter(featured=True).order_by('-list_date')[0:3]
  realtors = Realtor.objects.order_by('-hire_date')[:3]
  
  context = {
    'listing': listing,
    'object_list':featured,
    'realtors':realtors,
    
  }

  return render(request, 'single-properties.html', context)    
def agents(request):
    realtors = Realtor.objects.order_by('-hire_date')
    context = {
        'realtors': realtors,   
    } 
    return render(request, 'agents.html', context)
class AgentDetailView(DetailView):
    model = Realtor  
    template_name = 'agent-details.html'        

