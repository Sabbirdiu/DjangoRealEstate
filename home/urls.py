from django.urls import path
from .views import *

urlpatterns = [
    path('',index ,name='home' ),
    path('agents/',agents,name='agents' ),
    path('agents/<int:pk>/',AgentDetailView.as_view(),name ='agent-details'),
    path('listing/',listing,name='listings' ),
    path('listing/<int:id>',listingdetail, name='listing' ),
]
