from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from .models import Post,Comment,CommentForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from taggit.models import Tag
from django.template.defaultfilters import slugify
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
    # get post object
    post = get_object_or_404(Post,  slug=slug)
    news_featured = Post.objects.filter(featured=True).order_by('-timestamp')[0:4]
    posts = Post.objects.all()
   
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
    return render(request,
                  'news-details.html',
                  {'obj': post,
                  'news_object_list':news_featured,
                   'comments': comments,
                   'posts':posts,
                  
                   'comment_form': comment_form})
