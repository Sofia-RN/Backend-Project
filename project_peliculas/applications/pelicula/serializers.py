from rest_framework import serializers
from .models import Pelicula


class PeliculaSerializer(serializers.ModelSerializer):

    #Aqui sirve para que pongas los datos que desees devolver en el json 
    class Meta:
        model = Pelicula
        fields = ('__all__') #Trae todos los datos


