from django.db import models


class Role(models.Model):
    nombre_role = models.CharField(max_length=50)
