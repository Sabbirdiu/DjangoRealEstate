from rest_framework import serializers
from ..models import Listing

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('title','slug', 'city', 'state', 'price', 'servicetype', 'rent_agreement', 'bedrooms', 'bathrooms', 'sqft', 'photo_main','kitchen','video')

class listingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'
        lookup_field = 'slug'        