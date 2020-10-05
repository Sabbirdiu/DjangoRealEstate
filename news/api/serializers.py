from rest_framework import serializers
from ..models import Post

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','slug', 'photo_main','previous_post','next_post','timestamp')

class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        lookup_field = 'slug'        