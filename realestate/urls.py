
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from contact.views import *

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('news/',include('news.urls')),
    path('contact/',include('contact.urls')),

    path('about/',about,name='about'),

    
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('my-account/',profile,name='account'),
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='password_change_form.html'),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),name='password_change_done'),

    # api
    path('api/',include('home.api.urls')),
    path('api/news/',include('news.api.urls')),
    

  

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
