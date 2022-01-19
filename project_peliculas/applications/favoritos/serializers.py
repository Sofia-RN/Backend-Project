from rest_framework import serializers
from .models import User, Pelicula, Favoritos


class FavoritosSerializer(serializers.ModelSerializer):

    #Aqui sirve para que pongas los datos que desees devolver en el json 
    class Meta:
        model = Favoritos
        fields = ('__all__') #Trae todos los datos
