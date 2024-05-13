from django.views import View
from django.shortcuts import render, redirect
from usuarios.models import Usuario
import json
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import timedelta, datetime
# from django.contrib.auth.mixins import LoginRequiredMixin


# implementar LoginRequiredMixin
class Ver_Usuarios(View):
    template_name = "Usuarios.html"

    def get(self, request, *args, **kwargs):
        usuarios = Usuario.objects.all()
        return render(request, self.template_name, {"lista_usuarios": usuarios})

    def post(self, request, *args, **kwargs):
        if request.headers.get('Content-Type') == 'application/json':
            return RespuestaAJAX(request)
            # Manejar solicitud POST AJAX
            # Aquí puedes acceder a los datos enviados por AJAX utilizando request.POST o request.body
        else:
            Nombre = request.POST['Nombre']
            Numero = request.POST['numero_empleado']
            Contraseña = request.POST['Contraseña']
            # Correo = request.POST['Correo']
            usuario = Usuario.objects
            usuario.create_user(Numero, Nombre, Contraseña)
            return HttpResponseRedirect(reverse('usuarios:usuarios'))


def RespuestaAJAX(request):
    datos = json.loads(request.body)
    try:
        Accion = datos.get("Accion")
        switch = Acciones_Usuario(datos.get("Usuario"))
        print(datos.get("Usuario"))
        print(datos.get("Accion"))

    except Exception as e:
        # Manejo de la excepción
        return JsonResponse({'error': str(e)}, status=500)

        # Numero = request.POST['numero_empleado']
        # Contraseña = request.POST['Contraseña']
        # Accion = request.POST['Accion']
        # Correo = request.POST['Correo']
    # usuario.create_user(Numero, Nombre, Contraseña)
    return switch.ejecutar_opcion(Accion)


class Acciones_Usuario:
    def __init__(self, id):
        self.id = id
        self.usuario = Usuario.objects

    def Eliminar(self):
        objeto_a_modificar = self.usuario.get(id=self.id)
        objeto_a_modificar.delete()
        return JsonResponse({'resultado': "SIP"})

    def Bloquear(self):
        print("Estás en el caso 2")
        print("Estás en el caso eliminar ", self.id)
        # Suponiendo que deseas modificar el objeto con id=1
        objeto_a_modificar = self.usuario.get(id=self.id)
        # Cambia el valor del atributo deseado
        # Reemplaza 'nuevo_valor' por el valor que deseas asignar
        objeto_a_modificar.modified_at = datetime.now()

        objeto_a_modificar.is_active = False
        # Guarda los cambios en la base de datos
        objeto_a_modificar.save()
        return JsonResponse({'resultado': "Usuario Deshabilitado"})

    def Desbloquear(self):
        objeto_a_modificar = self.usuario.get(id=self.id)
        objeto_a_modificar.is_active = True
        objeto_a_modificar.save()
        return JsonResponse({'resultado': "Usuario Deshabilitado"})

    def default(self):
        print("Opción no válida")
        print("Estás en el caso eliminar")
        return JsonResponse({'resultado': "NOP"})

    def ejecutar_opcion(self, opcion):
        metodo = getattr(self, opcion, self.default)
        return metodo()
