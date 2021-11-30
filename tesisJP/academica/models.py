from django.db import models
#from bases.models import ClaseModelo
from pedagogica.models import Asignatura,Semestre

#Create your models here.
class TiposPersona(models.Model):
    tipo = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self): #lo que gresesara al consultar 
        return self.tipo

    class Meta:
        verbose_name_plural = 'tipo persona'

    def save(self):
        super(TiposPersona,self).save()


class Persona(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellidoPaterno = models.CharField(max_length=50, blank=False, null=False)
    apellidoMaterno = models.CharField(max_length=50, blank=False, null=False)
    curp = models.CharField(max_length=50, blank=False, null=False)
    
    tipoPersona= models.ForeignKey(TiposPersona, on_delete=models.CASCADE)


    def __str__(self): #lo que gresesara al consultar 
        return self.tipo

    class Meta:
        verbose_name_plural = 'Persona'

    def save(self):
        super(Persona,self).save()


class Docente(models.Model):
    cedulaProfecional = models.CharField(max_length=50, blank=False, null=False)
    
    tipoPersona= models.ForeignKey(Persona, on_delete=models.CASCADE)

     
    grupos= models.ManyToManyField(
        'grupo', blank=True, related_name="DocentesG"
    )

    asignaturas= models.ManyToManyField(
        'asignatura', blank=True, related_name="DocentesA"
    )


    def __str__(self): #lo que gresesara al consultar 
        return self.cedulaProfecional

    
    class Meta:
        verbose_name_plural = 'Cedula Profecional'

    def save(self):
        super(Docente,self).save()

class Grupo(models.Model):
    grupo = models.CharField(max_length=50, blank=False, null=False)

    semestre= models.ForeignKey(Semestre, on_delete=models.CASCADE)

    
    asignaturas= models.ManyToManyField(
        'asignatura', blank=True, related_name="GruposA"
    )


    def __str__(self): #lo que gresesara al consultar 
        return self.grupo

    class Meta:
        verbose_name_plural = 'Grupo'

    def save(self):
        super(Grupo,self).save()
