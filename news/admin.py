from django.contrib import admin
from .models import Author, Post

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Author)
admin.site.register(Post,ArticleAdmin)