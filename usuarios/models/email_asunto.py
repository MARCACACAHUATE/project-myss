from django.db import models


class Asunto(models.Model):
    # Puede se Aceptado o Rechazado
    Abreviatura = models.CharField(max_length=10)
    Tipo = models.CharField(max_length=20)

    def crear_asunto(self, tipo, abreviatura):
        NuevoAsunto = Asunto(Tipo=tipo, Abreviatura=abreviatura)
        NuevoAsunto.save()
        return NuevoAsunto
