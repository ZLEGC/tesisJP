from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf.global_settings import MEDIA_URL, STATIC_URL
from academica.models import Grupo,Asignatura
 
# Create your models here.
class User(AbstractUser):

    estatura = models.FloatField(blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    imagen = models.ImageField(
        upload_to='img/user/',blank=True, null=True
    )
    telefono= models.IntegerField(blank=True, null=True)
    grado =models.CharField(max_length=100, blank=True, null=True) 
    curp =models.CharField(max_length=19, blank=True, null=True)
    direccion = models.CharField(max_length=300, blank=True, null=True)
    cedula =models.CharField(max_length=50, blank=True, null=True)
    matricula=models.CharField(max_length=8, blank=True, null=True)


         
    grupos= models.ManyToManyField(
        Grupo, blank=True, related_name="DocentesG"
    )

    asignaturas= models.ManyToManyField(
        Asignatura, blank=True, related_name="DocentesA"
    )


    def get_image(slef):
        if self.imagen:
            return '{}{}'. format (MEDIA_URL, self.image)
        return '{}{}'. format(STATIC_URL,'img/empty.png' )


