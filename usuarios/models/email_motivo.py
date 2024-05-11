from django.db import models


class Motivo(models.Model):
    # En principio serian dos, rechazado o aceptado
    Asunto = models.ForeignKey("Asunto", on_delete=models.CASCADE)
    # Define el motivo predeterminado para una propuesta que es rechazada o aceptada
    Motivo = models.CharField(max_length=200)

    def crear_motivo(self, asunto, motivo):
        NuevoMotivo = Motivo(Asunto=asunto, Motivo=motivo)
        NuevoMotivo.save()
        return NuevoMotivo
