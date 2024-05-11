from django.views import View
from django.shortcuts import render
from usuarios.models import Usuario
# from django.contrib.auth.mixins import LoginRequiredMixin


# implementar LoginRequiredMixin
class Ver_Usuarios(View):
    template_name = "Usuarios.html"

    def get(self, request, *args, **kwargs):
        usuarios = Usuario.objects.all()
        for u in usuarios:
            print(u)
        return render(request, self.template_name, {"lista_usuarios": usuarios})
