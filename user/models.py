from django.db import models
from django.db.models.base import Model

# Create your models here.
class User(models.Model):
    nombre = models.CharField(max_length=50)
    apellidoP = models.CharField(max_length=50)
    apellidoM = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()
    email = models.EmailField(max_length=60)
    telefono = models.CharField(max_length=10)
    
