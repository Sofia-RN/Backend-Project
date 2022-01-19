from django.shortcuts import render

#Las de RestFramework para la API
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView, 
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)

#models
from .models import Favoritos
from applications.usuarios.models import User
from applications.pelicula.models import Pelicula

#serializer
from .serializers import (
    FavoritosSerializer
)


# Create your views here.
class FavDetailRetrieveUpdateView(RetrieveAPIView):
    serializer_class = FavoritosSerializer
    queryset = Favoritos.objects.all()  #para actualizar los datos pero que regrese los datos que ya tiene como el nombre y asi

class FavoritesCreateView(APIView):

    serializer_class = FavoritosSerializer

    def post(self, request, *args, **kwargs):

        user= request.data['user']
        usuario= User.objects.get(
            nombre= user
        )
        
        peliculas= request.data['pelicula']
        pelicula= Peliculas.objects.get(
            nombre= peliculas
        )
        print(pelicula,'adsasdads')
        # Favoritos.objects.create(
        #     user=usuario,
        #     pelicula=pelicula,
        # )
        return HttpResponse(json.dumps({'message': "Usuario Create"}), status=200) 