from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from propuestas.models import Propuesta
from propuestas.utils import Status
from django.core.mail import send_mail
from django.conf import settings


class PropuestasDetallesView(LoginRequiredMixin, View):
    login_url = "/login"
    template_name = "propuesta_detalles.html"

    def get(self, request, *args, **kwargs):
        id = self.kwargs['propuesta_id']
        print(f"Detalles de la propuesta {id}")

        propuesta = Propuesta.objects.get(id=id)
        print(propuesta)
        return render(request, self.template_name, {"propuesta_data": propuesta})

    def post(self, request, *args, **kwargs):
        id = self.kwargs['propuesta_id']
        propuesta = Propuesta.objects.get(id=id)
        propuesta.status = Status.ACEPTADA
        send_mail(subject=settings.EMAIL_HOST_ASUNTO, message="Enhorabuena su propuesta ha sido acepatada",
                  from_email=settings.EMAIL_HOST_USER, recipient_list=[propuesta.correo_personal,
                                                                       propuesta.correo_institucional])
        propuesta.save()
        return render(request, self.template_name, {"propuesta_data": propuesta})
