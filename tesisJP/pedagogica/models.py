from django.db import models

# Create your models here.
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey


class Competencias (models.Model):
    competencia =models.CharField(max_length=200, blank=False, null=False)
    descripcionCompetencia =models.CharField(max_length=400, blank=False, null=False)

    def __str__(self):
        return self.competencia
    class Meta:
        verbose_name_plural = 'Competencias'
    def save(self):
        super(Competencias,self).save()


class Ambitos(models.Model):
    descripcionAmb =models.CharField(max_length=200, blank=False, null=False)
    aCompetencia= models.ForeignKey(Competencias, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcionAmb
    class Meta:
        verbose_name_plural = 'Ambitos'
    def save(self):
        super(Ambitos,self).save()


class Perfil_Egreso(models.Model):
    descripcionPe =models.CharField(max_length=400, blank=False, null=False)

    ambito= models.ForeignKey(Ambitos, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcionPe 
    class Meta:
        verbose_name_plural = 'Perfil_Egresos'
    def save(self):
        super(Perfil_Egreso,self).save()


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
    

    def __str__(self): #lo que va a devolver de manera automatica
        return self.carrera 

    class Meta:
        verbose_name_plural = 'Carreras' #Consultar nombre plural
    
    def save(self):   #el metodo save va a guardar la informacion en estos campos
        super(Carrera,self).save()

        
class Plan_Estudio(models.Model):
    objetivo =models.CharField(max_length=400, blank=False, null=False)

    descripcionPEgre= models.ForeignKey(Perfil_Egreso, on_delete=models.CASCADE)    
    pCarrera= models.ForeignKey(Carrera, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.objetivo 
    class Meta:
        verbose_name_plural = 'Planes_Estudio'
    def save(self):
        super(Plan_Estudio,self).save()