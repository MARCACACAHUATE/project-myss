from django.db import models


class TipoPropuesta(models.Model):
    nombre_tipo = models.CharField(max_length=50)
