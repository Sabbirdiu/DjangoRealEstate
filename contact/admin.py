from django.contrib import admin
from .models import About,Partnars,Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name',  'email', 'contact_date')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'email', )
  list_per_page = 25
admin.site.register(About)
admin.site.register(Partnars)
admin.site.register(Contact,ContactAdmin)