from rest_framework import serializers
from ..models import Listing,Realtor

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('title','slug', 'city', 'state', 'price', 'servicetype', 'rent_agreement', 'bedrooms', 'bathrooms', 'sqft', 'photo_main','kitchen','video','list_date')

class listingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'
        lookup_field = 'slug'        

class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realtor
        fields = '__all__'        
