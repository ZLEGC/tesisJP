from django.db import models
#from bases.models import ClaseModelo
from pedagogica.models import Asignatura,Semestre

#Create your models here.


class Grupo(models.Model):
    grupo = models.CharField(max_length=50, blank=False, null=False)

    semestre= models.ForeignKey(Semestre, on_delete=models.CASCADE)

    
    asignaturas= models.ManyToManyField(
        Asignatura, blank=True, related_name="GruposA"
    )


    def __str__(self): #lo que gresesara al consultar 
        return self.grupo

    class Meta:
        verbose_name_plural = 'Grupo'

    def save(self):
        super(Grupo,self).save()
