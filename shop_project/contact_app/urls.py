from django.urls import path
from . import views

app_name = 'contact_app'


urlpatterns = [
	path('contact_form/', views.index, name='contact_form'),
	path('contact_form/success/', views.success, name='success'),
]