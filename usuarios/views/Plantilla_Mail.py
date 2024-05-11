from django.views import View
from django.shortcuts import render
from django.conf import settings
from usuarios.models import Email
# from django.contrib.auth.mixins import LoginRequiredMixin


# implementar LoginRequiredMixin
class Plantilla_Mail(View):
    template_name = "PlantillaCorreo.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        asunto = request.POST['Asunto']
        saludo = request.POST['Saludo']
        firma = request.POST['Firma']
        tipo = request.POST['tipo']
        if (tipo == "Aceptada"):
            tipo = 1
        else:
            tipo = 2
        nuevo_mail = Email().create_base(asunto, saludo, firma, tipo)
        print(nuevo_mail)
        return render(request, self.template_name)
