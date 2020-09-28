from django.urls import path
from .views import *

urlpatterns = [
    path('',index ),
    path('agents/',agents ),
    path('agents/<int:pk>/',AgentDetailView.as_view(),name ='agent-details'),
    path('listing/',listing ),
    path('listing/<int:id>',listingdetail, name='listing' ),
]
