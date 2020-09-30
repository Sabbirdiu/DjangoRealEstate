from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()
from ckeditor.fields import  RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm
from django import forms
# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    overview = RichTextField(null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    featured = models.BooleanField()
    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'slug': self.slug
        })        
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=200, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # manually deactivate inappropriate comments from admin site
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies',on_delete=models.CASCADE)

    class Meta:
        # sort comments in chronological order by default
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')        