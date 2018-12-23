from django.urls import path
from . import views

app_name = 'contact_app'

urlpatterns = [
  path('', views.contact, name='contact'),
  path('success/', views.success, name='success'),
]