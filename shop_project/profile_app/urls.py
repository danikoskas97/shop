from django.urls import path
from . import views


app_name = 'profile_app'

urlpatterns = [
# le name ici va dans la pages html pour remplacer pour le formulaire
path('signup/', views.signup, name='signup'),
path('login/', views.login_auth, name='login'),
path('logout_auth/', views.logout_auth, name='logout_auth'),
path('profile/<int:user_id>/', views.profile, name='profile'),
path('profile/<int:user_id>/edit/', views.edit_profile, name='edit_profile'),
]