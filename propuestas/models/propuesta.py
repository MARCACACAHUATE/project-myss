from django.db import models


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
    status = models.CharField(max_length=30)
    descripcion_respuesta = models.TextField()
    archivo_propuesta = models.TextField()
    tipo_propuesta_id = models.ForeignKey(
        "TipoPropuesta", on_delete=models.CASCADE)
    supervisor_id = models.ForeignKey(
        "usuarios.Usuario", on_delete=models.CASCADE)
