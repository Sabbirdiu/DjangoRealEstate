from django.contrib import admin

# Register your models here.
from home.models import Realtor,Listing,Comment
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('name','email')
    prepopulated_fields = {'slug': ('name',)}
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title','realtor')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Realtor,RealtorAdmin)
admin.site.register(Listing,ListingAdmin)
admin.site.register(Comment)