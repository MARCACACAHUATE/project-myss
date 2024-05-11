from django.views import View
from django.shortcuts import render
from usuarios.models import Asunto
# from django.contrib.auth.mixins import LoginRequiredMixin


# implementar LoginRequiredMixin
class Crear_Asunto(View):
    template_name = "NuevoAsunto.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        Descripción = request.POST['Tipo']
        asunto = Asunto().crear_asunto(asunto=Descripción)
        print(asunto)
        return render(request, self.template_name)
