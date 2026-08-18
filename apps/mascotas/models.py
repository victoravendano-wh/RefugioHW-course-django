from django.db import models

from apps.adopciones.models import Persona

# Create your models here.

class Vacuna(models.Model):
	nombre = models.CharField(max_length=60)
	def __str__(self):
		return '{}'.format(self.nombre)
	
class Mascota(models.Model):
	nombre = models.CharField(max_length=50)
	sexo = models.CharField(max_length=60)
	edad_aproximada = models.IntegerField()
	fecha_rescate = models.DateField()
	persona = models.ForeignKey(Persona, null = True, on_delete = models.CASCADE, blank=True)
	vacuna = models.ManyToManyField(Vacuna, null=True, blank=True)
	imagen = models.ImageField(upload_to='images/', blank=True, null=True)
