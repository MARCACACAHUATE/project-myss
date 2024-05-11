from django.views import View
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# from django.contrib.auth.mixins import LoginRequiredMixin


# implementar LoginRequiredMixin
class CorreoPlantilla(View):
    template_name = "correo.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        asunto = request.POST['nombre']
        to = request.POST['email']
        mensaje = request.POST['mensaje']
        print(settings.EMAIL_HOST_USER)
        print(asunto)
        print(to)
        print(mensaje)
        send_mail(subject=asunto, message=mensaje,
                  from_email=settings.EMAIL_HOST_USER, recipient_list=[to])
        return render(request, self.template_name)
