from django.db import models
from django.utils import timezone
from propuestas.utils import Status


class Propuesta(models.Model):
    nombre = models.CharField(max_length=100)
    no_empleado = models.CharField(max_length=8)
    correo = models.EmailField()
    area = models.CharField(max_length=50)
    puesto = models.CharField(max_length=70)
    correo_personal = models.EmailField()
    correo_institucional = models.EmailField()
    telefono = models.CharField(max_length=10)
    torre_perteneciente = models.CharField(max_length=100)
    compromiso = models.TextField()
    status = models.CharField(max_length=30, default=Status.PENDIENTE)
    descripcion_respuesta = models.TextField()
    motivo = models.ForeignKey(
        "usuarios.Motivo", null=True, blank=True, on_delete=models.SET_DEFAULT, default=None)
    archivo_propuesta = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    tipo_propuesta_id = models.ForeignKey(
        "TipoPropuesta", on_delete=models.CASCADE)
    supervisor_id = models.ForeignKey(
        "usuarios.Usuario", null=True, blank=True, on_delete=models.SET_NULL)
