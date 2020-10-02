from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from .models import Realtor,Listing,Comment,CommentForm
from news.models import Post
from django.views.generic import DetailView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from contact.models import Partnars
from .choices import bedroom_choices,bathroom_choices,price_choices,state_choices,type_choices
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
        'partnar':partnar,
        'bedroom_choices':bedroom_choices,
        'bathroom_choices':bathroom_choices,
        'price_choices':price_choices,
        'state_choices':state_choices,
        'type_choices':type_choices
       
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
    post = get_object_or_404(Listing, slug=slug)
    featured = Listing.objects.filter(featured=True).order_by('-list_date')[0:3]
    realtors = Realtor.objects.order_by('-hire_date')[:3]
# list of active parent comments
    comments = post.comments.filter(active=True, parent__isnull=True)
    if request.method == 'POST':
        # comment has been added
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_obj = None
            # get parent comment id from hidden input
            try:
                # id integer e.g. 15
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            # if parent_id has been submitted get parent_obj id
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                # if parent object exist
                if parent_obj:
                    # create replay comment object
                    replay_comment = comment_form.save(commit=False)
                    # assign parent_obj to replay comment
                    replay_comment.parent = parent_obj
            # normal comment
            # create comment object but do not save to database
            new_comment = comment_form.save(commit=False)
            # assign ship to the comment
            new_comment.post = post
            # save
            new_comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()
  
    context = {
        'listing': post,
        'object_list':featured,
        'realtors':realtors,
        'comments': comments,
        
        'comment_form': comment_form,
        
    }

    return render(request, 'single-properties.html', context)    
def agents(request):
    realtor = Realtor.objects.order_by('-hire_date')
    paginator = Paginator(realtor, 1)
    page = request.GET.get('page')
    realtors = paginator.get_page(page)
    context = {
        'realtors': realtors,   
    } 
    return render(request, 'agents.html', context)
class AgentDetailView(DetailView):
    model = Realtor  
    template_name = 'agent-details.html'        

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    # latest = Listing.objects.order_by('-list_date')[0:6]
    if 'keywords' in request.GET:
      keywords = request.GET['keywords']
      if keywords:
        queryset_list = queryset_list.filter(description__icontains=keywords)
  # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)  
  # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
           queryset_list = queryset_list.filter(state__iexact=state)   
    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
           queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)        
    # Bathrooms
    if 'bathrooms' in request.GET:
        bathrooms = request.GET['bathrooms']
        if bathrooms:
           queryset_list = queryset_list.filter(bathrooms__lte=bathrooms)      
    # Types
    if 'types' in request.GET:
        types = request.GET['types']
        if types:
           queryset_list = queryset_list.filter(type__lte=types)                                

    context={
    'bedroom_choices':bedroom_choices,
    'bathroom_choices':bathroom_choices,
    'price_choices':price_choices,
    'state_choices':state_choices,
    'type_choices':type_choices,
    'listings':queryset_list
    }
    return render(request,'search.html',context)