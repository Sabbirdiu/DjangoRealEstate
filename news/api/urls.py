from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsView.as_view()),
    path('<slug>/', NewsDetailsView.as_view()),
]