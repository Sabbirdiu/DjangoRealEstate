from django.shortcuts import render
from .models import Post
# Create your views here.
def post(request):
    post_list = Post.objects.order_by('-timestamp')
    context = {
        'post_list':post_list
    }
    return render(request,'news.html',context)