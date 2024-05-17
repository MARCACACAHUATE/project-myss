from django.views import View
from django.shortcuts import render
from usuarios.models import Motivo, Asunto
import json
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

# from django.contrib.auth.mixins import LoginRequiredMixin


# implementar LoginRequiredMixin
class Ver_Motivo(View):
    template_name = "Motivos.html"

    def get(self, request, *args, **kwargs):
        motivo = Motivo.objects.all()
        asuntos = Asunto.objects.all()
        return render(request, self.template_name, {"lista_motivos": motivo, "lista_asuntos": asuntos})

    def post(self, request, *args, **kwargs):
        if request.headers.get('Content-Type') == 'application/json':
            return RespuestaAJAX(request)
            # Manejar solicitud POST AJAX
            # Aquí puedes acceder a los datos enviados por AJAX utilizando request.POST o request.body
        else:
            asunto = request.POST['tipo']
            motivo = request.POST['Motivo']
            clave = Asunto.objects.get(id=asunto)
            nuevomotivo = Motivo().crear_motivo(asunto=clave, motivo=motivo)
            print(nuevomotivo)
            return HttpResponseRedirect(reverse('usuarios:VerMotivo'))


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
        self.motivo = Motivo.objects

    def Eliminar(self):
        objeto_a_modificar = self.motivo.get(id=self.id)
        objeto_a_modificar.delete()
        return JsonResponse({'resultado': "SIP"})

    def Bloquear(self):
        print("Estás en el caso 2")
        print("Estás en el caso eliminar ", self.id)
        # Suponiendo que deseas modificar el objeto con id=1
        objeto_a_modificar = self.motivo.get(id=self.id)
        # Cambia el valor del atributo deseado
        # Reemplaza 'nuevo_valor' por el valor que deseas asignar
        objeto_a_modificar.is_active = False
        # Guarda los cambios en la base de datos
        objeto_a_modificar.save()
        return JsonResponse({'resultado': "motivo Deshabilitado"})

    def default(self):
        print("Opción no válida")
        print("Estás en el caso eliminar")
        return JsonResponse({'resultado': "NOP"})

    def ejecutar_opcion(self, opcion):
        metodo = getattr(self, opcion, self.default)
        return metodo()
