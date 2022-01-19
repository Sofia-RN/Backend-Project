
from model_utils.models import TimeStampedModel
from django.db import models 

# Create your models here.

class Pelicula(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=120, blank=True, null=True)
    fecha = models.DateField('Fecha',  blank=True, null=True)
    descripcion = models.CharField('Descripcion', max_length=50, blank=True, null=True)
    rango = models.PositiveIntegerField('Rango', blank=True, null=True)
    director = models.CharField('Director', max_length=100, blank=True, null=True)
    autores = models.CharField('Autores', max_length=120, blank=True, null=True)
    duracion = models.CharField('Duracion', max_length=100, blank=True, null=True)
    imagen = models.TextField('Imagen', max_length=100, blank=True, null=True) #modificar luego
    
    class Meta:
        verbose_name = 'Pelicula'
        verbose_name_plural = 'Peliculas'
    
    def __str__(self):
        return self.nombre
