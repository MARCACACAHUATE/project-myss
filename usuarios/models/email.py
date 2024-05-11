from django.db import models
from django.core.mail import send_mail
from django.conf import settings


class Email(models.Model):
    # Esta es una llave foranea al motivo predeterminado para una propuesta
    Motivo = models.ForeignKey("Motivo", on_delete=models.CASCADE)
    # Este seria el espacio para el mensaje personalizado del analista
    Comentarios = models.CharField(max_length=100)

    def send_mail(self, destinatario):
        """
        Crea un usuario con el nombre, numero de empleado y password.
        """
        mensaje = [self.Motivo, self.Comentarios]
        cuerpo = "\n\n".join(mensaje)
        try:
            send_mail(subject=self.Motivo, message=cuerpo,
                      from_email=settings.EMAIL_HOST_USER, recipient_list=[destinatario])
            resultado = "Correo enviado exitosamente"
        except Exception as e:
            # Manejo de cualquier otra excepción no especificada
            resultado = "Error:", e
        return resultado

    def create_base(self, asunto, saludo, firma, tipo):
        """
        Crea un SuperUsuario con el nombre, numero de empleado y password.
        """
        email = Email(asunto=asunto, saludo=saludo,
                      firma=firma, tipo=tipo)
        email.save()
        return email
