from django.views import View
from django.shortcuts import render
from usuarios.models import Asunto
# from django.contrib.auth.mixins import LoginRequiredMixin


# implementar LoginRequiredMixin
class Ver_Asuntos(View):
    template_name = "Asunto.html"

    def get(self, request, *args, **kwargs):
        asunto = Asunto.objects.all()
        return render(request, self.template_name, {"lista_asuntos": asunto})
