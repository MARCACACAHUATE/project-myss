from django.db import models


class Asunto(models.Model):
    # Puede se Aceptado o Rechazado
    Tipo = models.CharField(max_length=10)

    def crear_asunto(self, asunto):
        NuevoAsunto = Asunto(Tipo=asunto)
        NuevoAsunto.save()
        return NuevoAsunto
