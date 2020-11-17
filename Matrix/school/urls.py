from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='school-home'),
    path('registration/', views.registration, name='school-registration'),
    path('maps/', views.maps, name='school-map'),

]