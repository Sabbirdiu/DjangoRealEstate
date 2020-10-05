from django.urls import path
from .views import *
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('realestate', RealestateViewSet)

urlpatterns = [
    path('', ListingsView.as_view()),
    # path('search', SearchView.as_view()),
    path('<slug>/', ListingView.as_view()),
    path('listings/', RealtorListView.as_view()),
    # path('topseller', TopSellerView.as_view()),
    path('agents/<pk>/', RealtorView.as_view()),
]
# urlpatterns += router.urls