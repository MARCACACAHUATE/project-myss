from django.db import models


class Motivo(models.Model):
    # En principio serian dos, rechazado o aceptado
    Asunto = models.ForeignKey("Asunto", on_delete=models.CASCADE)
    # Define el motivo predeterminado para una propuesta que es rechazada o aceptada
    Titulo = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=200)

    def crear_motivo(self, asunto, titulo, motivo):
        NuevoMotivo = Motivo(Asunto=asunto, Titulo=titulo, Descripcion=motivo)
        NuevoMotivo.save()
        return NuevoMotivo
