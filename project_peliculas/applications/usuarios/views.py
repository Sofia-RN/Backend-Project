import json
from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import (
    CreateUserSerializer, LoginUserSerializer
)

class UserCreateView(APIView):
     
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs): 

        passwd_hash = make_password(request.data['password'] )

        user = User.objects.create(
            username=request.data['username'],
            nombre= request.data['nombre'],
            email= request.data['email'],
            edad= request.data['edad'],
            password= passwd_hash,
        )

        return HttpResponse(json.dumps({'message': "Usuario Creado"}), status=200)  

class UserLoginApiView(APIView):

    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs): 
        email = request.data['email']
        usuario= User.objects.filter(email= email)

        if len(usuario) ==0:
            return HttpResponse(json.dumps({'Error': "El usuario no existe",}), status=200)  

        else:
            verificate = check_password(str(request.data['password']),str(usuario[0].password))

            if verificate ==  True:
                return HttpResponse(json.dumps({
                                                'username': str(usuario[0].username), 
                                                'nombre': str(usuario[0].nombre), 
                                                'email':str(usuario[0].email), 
                                                'Acceso':True}), 
                                                status=200)  
            else:
                return HttpResponse(json.dumps({'Error': "La contraseña es invalida",}), status=200)       
            
            
