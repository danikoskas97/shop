from django.contrib import admin
from django.urls import path, include
from shop_app import views
from contact_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop_app/', include('shop_app.urls')),
    path('contact_app/', include('contact_app.urls')),
  
]