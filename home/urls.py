from django.urls import path
from .views import *

urlpatterns = [
    path('',index ,name='home' ),
    path('agents/',agents,name='agents' ),
    path('agents/<slug:slug>/',AgentDetailView.as_view(),name ='agent-details'),
    path('listings/',listing,name='listings' ),
    path('listing/<slug:slug>/',listingdetail, name='listing' ),
]
