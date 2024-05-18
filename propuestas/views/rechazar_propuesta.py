from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from propuestas.forms import RechazarPropuestaForm
from propuestas.models import Propuesta
from propuestas.utils import Status
from usuarios.models import Motivo
from django.core.mail import send_mail
from django.conf import settings


class RechazarPropuestaView(LoginRequiredMixin, View):
    login_url = "/login"
    template_name = "rechazar_propuesta.html"

    def get(self, request, *args, **kwargs):
        form = RechazarPropuestaForm()
        motivos = Motivo.objects.all()

        context = {
            "propuesta_id": self.kwargs["propuesta_id"],
            "form": form,
            "motivos_rechazon": motivos
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        propuesta_id = self.kwargs["propuesta_id"]

        propuesta = Propuesta.objects.get(id=propuesta_id)

        form = RechazarPropuestaForm(request.POST)

        context = {
            "propuesta_id": propuesta_id,
            "form": form
        }

        if form.is_valid():
            data = form.cleaned_data
            motivo = Motivo.objects.get(Titulo=data["motivo_rechazo"])
            propuesta.descripcion_respuesta = data["descripcion"]
            propuesta.status = Status.RECHAZADA
            propuesta.motivo = motivo
            mensaje = [motivo.Titulo, motivo.Descripcion,
                       propuesta.descripcion_respuesta]
            cuerpo = "\n\n".join(mensaje)
            send_mail(subject=settings.EMAIL_HOST_ASUNTO, message=cuerpo,
                      from_email=settings.EMAIL_HOST_USER, recipient_list=[propuesta.correo_personal,
                                                                           propuesta.correo_institucional])
            propuesta.save()

        else:
            print("Formulario Invalido")
            return render(request, self.template_name, context)

        return redirect(f"/propuestas/{propuesta_id}/")
