from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.base import Model

# Create your models here.
class User(models.Model):
    nombre = models.CharField('Nombre del usuario', max_length=50)
    apellidoP = models.CharField('Apellido paterno del usuario', max_length=50)
    apellidoM = models.CharField('Apellido materno del usuario', max_length=50)
    edad = models.PositiveIntegerField('Edad del usuario')
    email = models.EmailField('Email del usuario',max_length=60)
    telefono = models.CharField('Telefono', max_length=10, validators=[MinLengthValidator(10)])
    
