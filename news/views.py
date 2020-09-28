from django.shortcuts import render
from .models import Post
# Create your views here.
def post(request):
    news = Post.objects.order_by('-timestamp')
    context = {
        'post':news
    }
    return render(request,'news.html')