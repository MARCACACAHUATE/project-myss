from django.views import View
from django.shortcuts import render
from usuarios.models import Asunto
import json
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

# from django.contrib.auth.mixins import LoginRequiredMixin


# implementar LoginRequiredMixin
class Ver_Asuntos(View):
    template_name = "Asunto.html"

    def get(self, request, *args, **kwargs):
        asunto = Asunto.objects.all()
        return render(request, self.template_name, {"lista_asuntos": asunto})

    def post(self, request, *args, **kwargs):
        if request.headers.get('Content-Type') == 'application/json':
            return RespuestaAJAX(request)
            # Manejar solicitud POST AJAX
            # Aquí puedes acceder a los datos enviados por AJAX utilizando request.POST o request.body
        else:
            Descripción = request.POST['Descripcion']
            Titulo = request.POST['Abreviatura']
            asunto = Asunto().crear_asunto(tipo=Descripción, abreviatura=Titulo)
            print(asunto)
            return HttpResponseRedirect(reverse('usuarios:VerAsunto'))


def RespuestaAJAX(request):
    datos = json.loads(request.body)
    try:
        Accion = datos.get("Accion")
        switch = Acciones_Motivo(datos.get("Usuario"))
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


class Acciones_Motivo:
    def __init__(self, id):
        self.id = id
        self.motivo = Asunto.objects

    def Eliminar(self):
        objeto_a_modificar = self.motivo.get(id=self.id)
        objeto_a_modificar.delete()
        return JsonResponse({'resultado': "SIP"})

    def default(self):
        print("Opción no válida")
        print("Estás en el caso eliminar")
        return JsonResponse({'resultado': "NOP"})

    def ejecutar_opcion(self, opcion):
        metodo = getattr(self, opcion, self.default)
        return metodo()
