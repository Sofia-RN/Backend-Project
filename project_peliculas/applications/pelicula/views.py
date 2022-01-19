from django.shortcuts import render
from django.db.models import Q
from rest_framework.generics import ListAPIView
#models
from .models import Pelicula

#serializer
from .serializers import PeliculaSerializer


class PeliListApiView(ListAPIView):
    #serializar los datos
    serializer_class = PeliculaSerializer

    def get_queryset(self):
        return Pelicula.objects.all()


class PeliculaBuscarApiView(ListAPIView):
        #serializar los datos
    serializer_class = PeliculaSerializer
    
    def get_queryset(self):
        #Filtrar datos
        kword = self.kwargs['kword']
        return Pelicula.objects.filter(
            Q(nombre__icontains=kword) | Q(rango__icontains=kword)
        )


class PeliculaFiltrarApiView(ListAPIView):
        #serializar los datos
    serializer_class = PeliculaSerializer
    
    def get_queryset(self):
        #Filtrar datos
        kword = self.kwargs['kword']
        return Pelicula.objects.filter(
            fecha__icontains=kword
        )

