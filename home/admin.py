from django.contrib import admin

# Register your models here.
from home.models import Realtor,Listing

admin.site.register(Realtor)
admin.site.register(Listing)