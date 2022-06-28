from django.db import models

# Create your models here.

class Villa_olimpica(models.Model):

    nombre=models.CharField(max_length=40)
    ubicacion=models.CharField(max_length=40)
    numero=models.IntegerField()
    fundacion=models.DateField()
    
class Disciplina(models.Model):

    nombre= models.CharField(max_length=40)
    se_juega_con_balon=models.BooleanField()

class Deportista(models.Model):

    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email=models.EmailField()


