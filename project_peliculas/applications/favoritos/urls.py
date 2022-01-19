
from django.urls import path, re_path

from . import views

app_name = 'fav_app'

urlpatterns = [
    path(
        'api/favoritos/detail/<pk>/',
        views.FavDetailRetrieveUpdateView.as_view(),
    ),
    path(
        'api/favoritos/created/',
        views.FavoritesCreateView.as_view(),
    ),

    
]