from django.urls import path
from .views import *

urlpatterns = [
    path('',post,name='news'),
    path('<slug:slug>/',newsdetails, name='post-detail' ),

]