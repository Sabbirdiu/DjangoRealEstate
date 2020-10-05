from rest_framework import serializers
from ..models import Listing

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('title', 'city', 'state', 'price', 'servicetype', 'rent_agreement', 'bedrooms', 'bathrooms', 'sqft', 'photo_main', 'slug','kitchen','video')