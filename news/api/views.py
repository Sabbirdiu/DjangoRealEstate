from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from  ..models import Post
from .serializers import NewsSerializer, NewsDetailSerializer
from datetime import datetime, timezone, timedelta

class NewsView(ListAPIView):
    queryset = Post.objects.all()
    # permission_classes = (permissions.AllowAny, )
    serializer_class = NewsSerializer
    lookup_field = 'slug'
   
class NewsDetailsView(RetrieveAPIView):
    queryset = Post.objects.order_by('-timestamp')
    serializer_class = NewsDetailSerializer
    lookup_field = 'slug'