from django.views import View
from django.shortcuts import render
from usuarios.models import Motivo
# from django.contrib.auth.mixins import LoginRequiredMixin


# implementar LoginRequiredMixin
class Ver_Motivo(View):
    template_name = "Motivos.html"

    def get(self, request, *args, **kwargs):
        motivo = Motivo.objects.all()
        return render(request, self.template_name, {"lista_motivos": motivo})
