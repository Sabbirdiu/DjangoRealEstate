from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.
def post(request):
    post_list = Post.objects.order_by('-timestamp')
    context = {
        'post_list':post_list
    }
    return render(request,'news.html',context)

def newsdetails(request,slug):
    post_detail = get_object_or_404(Post, slug=slug)
  
    context = {
        'obj': post_detail,
        
    }

    return render(request, 'news-details.html', context) 

