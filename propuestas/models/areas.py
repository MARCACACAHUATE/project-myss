from django.db import models


class Area(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
