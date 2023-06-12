from django.db import models

# Create your models here.


class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Rutinas(models.Model):
    nombre = models.CharField(max_length=40)
    rutina = models.TextField()

class Alimentos(models.Model):
    nombre = models.CharField(max_length=40)
    proteina = models.CharField(max_length=20)