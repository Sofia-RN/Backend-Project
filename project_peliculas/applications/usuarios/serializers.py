from rest_framework import serializers
from .models import User


class CreateUserSerializer(serializers.ModelSerializer):

    #Aqui sirve para que pongas los datos que desees devolver en el json 
    class Meta:
        model = User
        fields = ('__all__') #Trae todos los datos

class LoginUserSerializer(serializers.Serializer):

    email = serializers.CharField()
    password = serializers.CharField()
