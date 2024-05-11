from django.views import View
from django.shortcuts import render
from usuarios.models import Motivo, Asunto
# from django.contrib.auth.mixins import LoginRequiredMixin


# implementar LoginRequiredMixin
class Crear_Motivo(View):
    template_name = "NuevoMotivo.html"

    def get(self, request, *args, **kwargs):
        asuntos = Asunto.objects.all()
        print(asuntos)
        return render(request, self.template_name, {"lista_asuntos": asuntos})

    def post(self, request, *args, **kwargs):
        asunto = request.POST['tipo']
        motivo = request.POST['motivo']
        clave = Asunto.objects.get(id=asunto)
        nuevomotivo = Motivo().crear_motivo(asunto=clave, motivo=motivo)
        print(nuevomotivo)
        return render(request, "Motivos.html")
