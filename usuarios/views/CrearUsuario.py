from django.views import View
from django.shortcuts import render
from usuarios.models import Usuario
# from django.contrib.auth.mixins import LoginRequiredMixin


# implementar LoginRequiredMixin
class Crear_Usuarios(View):
    template_name = "NuevoUsuario.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        Nombre = request.POST['Nombre']
        Numero = request.POST['Numero']
        Contraseña = request.POST['Contraseña']
        Correo = request.POST['Correo']
        usuario = Usuario.objects
        usuario.create_user(Nombre, Numero, Contraseña, Correo)
        return render(request, self.template_name)
