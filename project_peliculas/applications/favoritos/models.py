from model_utils.models import TimeStampedModel
from django.db import models
from applications.pelicula.models import Pelicula
from applications.usuarios.models import User

# Create your models here.


class Favoritos(TimeStampedModel):
    
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='user_fav')

    pelicula = models.ForeignKey(
        Pelicula, 
        on_delete=models.CASCADE,
        related_name='Peliculas_fav')
    
    def __str__(self):
        return self.pelicula.nombre + ' - ' + self.user.nombre