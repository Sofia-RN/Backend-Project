
from django.urls import path, re_path

from . import views

app_name = 'pelicula_app'

urlpatterns = [

    path(
        'api/pelicula/search/<kword>/',
        views.PeliculaBuscarApiView.as_view(),
    ),
    path(
        'api/pelicula/filtrar/<kword>/',
        views.PeliculaFiltrarApiView.as_view(),
    ),
    path(
        'api/peliculas/',
        views.PeliListApiView.as_view(),
    ),

]