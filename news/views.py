from django.shortcuts import render,get_object_or_404
from .models import Post
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def post(request):
    post_list = Post.objects.order_by('-timestamp')
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings':paged_listings
    }
    return render(request,'news.html',context)

def newsdetails(request,slug):
    post_detail = get_object_or_404(Post, slug=slug)
  
    context = {
        'obj': post_detail,
        
    }

    return render(request, 'news-details.html', context) 

