from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='profile'),
    path('card', views.card, name='card'),
    path('create_card', views.create_card, name='create_card'),
]