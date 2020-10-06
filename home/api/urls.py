from django.urls import path
from .views import *

urlpatterns = [
    path('listings/', ListingsView.as_view()),
    
    path('listings/<slug>/', ListingView.as_view()),
    path('agents/', RealtorListView.as_view()),

    path('agents/<pk>/', RealtorView.as_view()),
]
