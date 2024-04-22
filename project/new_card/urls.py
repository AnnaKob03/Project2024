from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_card_home, name='new_card_home'),
    path('create', views.create, name='create'),
    path('ajax/technology-options/', views.technology_options, name='technology-options'),
]