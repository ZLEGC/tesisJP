from django.db import models

# Create your models here.
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

class Plan_Estudio(models.Model):
    objetivo =models.CharField(max_length=400, blank=False, null=False)
    perfilEgreso =models.CharField(max_length=400, blank=False, null=False)
    carreraAsig =models.CharField(max_length=400, blank=False, null=False)
    recomendacionesMet = models.CharField(max_length=400, blank=False, null=False)
    procedimientosEval =models.CharField(max_length=400, blank=False, null=False)
    procedimientosAcre =models.CharField(max_length=400, blank=False, null=False)
    certificacionEst =models.CharField(max_length=400, blank=False, null=False)
    perfilE =models.CharField(max_length=400, blank=False, null=False)
    complementarias =models.CharField(max_length=400, blank=False, null=False)
    firmas =models.CharField(max_length=100, blank=False, null=False)
    direccionEscuela =models.CharField(max_length=200, blank=False, null=False)



    def __str__(self):
        return self.objetivo 
    class Meta:
        verbose_name_plural = 'Planes_Estudio'
    def save(self):
        super(Plan_Estudio,self).save()


class Asignatura(models.Model):
    asignatura = models.CharField(max_length=100, blank=False, null=False)
    contenido =models.CharField(max_length=100, blank=False, null=False)
    totalHsTeoricas =models.FloatField(blank=False, null=False)
    totalHsPracticas =models.FloatField(blank=False, null=False)
    total =models.FloatField(blank=False, null=False)
    creditos =models.FloatField(blank=False, null=False)

    def __str__(self):
        return self.asignatura 
    class Meta:
        verbose_name_plural = 'Asignaturas'
    def save(self):
        super(Asignatura,self).save()


class Ejes(models.Model):
    ejes =models.CharField(max_length=100, blank=False, null=False)

    asignatura= models.ForeignKey(Asignatura, on_delete=models.CASCADE)

    def __str__(self):
        return self.ejes 
    class Meta:
        verbose_name_plural = 'Ejes'
    def save(self):
        super(Ejes,self).save()

class Semestre(models.Model):
    semestre =models.CharField(max_length=100, blank=False, null=False)

    ejes= models.ForeignKey(Ejes, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.semestre 
    class Meta:
        verbose_name_plural = 'Semestres'
    def save(self):
        super(Semestre,self).save()

class Ano(models.Model):
    ano = models.IntegerField(blank=False, null=False)

    semestre= models.ForeignKey(Semestre, on_delete=models.CASCADE)

    def __str__(self):
        return self.ano 
    class Meta:
        verbose_name_plural = 'Anos'
    def save(self):
        super(Ano,self).save()

class Carrera(models.Model):
    carrera = models.CharField(max_length=100, blank=False, null=False)
    nom_corto = models.CharField(max_length=100, blank=False, null=False)

    #Relacion hacia la tabla de año
    ano =models.ForeignKey(Ano, on_delete=models.CASCADE)
    Plan_Estudio= models.ForeignKey(Plan_Estudio, on_delete=models.CASCADE)

    def __str__(self): #lo que va a devolver de manera automatica
        return self.carrera 

    class Meta:
        verbose_name_plural = 'Carreras' #Consultar nombre plural
    
    def save(self):   #el metodo save va a guardar la informacion en estos campos
        super(Carrera,self).save()

    class Perfil_Egreso(models.Model):
        perfilEgre =models.CharField(max_length=100, blank=False, null=False)
