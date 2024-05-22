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
        return render(request, self.template_name, {"lista_asuntos": asuntos, "lista_motivos": motivo})

    def post(self, request, *args, **kwargs):
        if request.headers.get('Content-Type') == 'application/json':
            return RespuestaAJAX(request)
            # Manejar solicitud POST AJAX
            # Aquí puedes acceder a los datos enviados por AJAX utilizando request.POST o request.body
        else:
            asunto = request.POST['tipo']
            titulo = request.POST['Titulo']
            motivo = request.POST['Descripcion']            
            clave = Asunto.objects.get(id=asunto)
            print(asunto)
            print(clave)
            nuevomotivo = Motivo().crear_motivo(asunto=clave, motivo=motivo, titulo=titulo)
            print(nuevomotivo)
            return HttpResponseRedirect(reverse('usuarios:VerMotivo'))


"""Asunto = models.ForeignKey("Asunto", on_delete=models.CASCADE)
    Motivo = models.CharField(max_length=200)
"""

FormularioModificar = {"m_tipo": "Asunto", "m_Titulo": "Titulo",
                       "m_Descripcion": "Descripcion"}


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
    return switch.ejecutar_opcion(Accion, datos)


class Acciones_Motivo:
    def __init__(self, id):
        self.id = id
        self.motivo = Motivo.objects

    def Eliminar(self, datos):
        objeto_a_modificar = self.motivo.get(id=self.id)
        objeto_a_modificar.delete()
        return JsonResponse({'resultado': "SIP"})

    def Bloquear(self, datos):
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

    def Modificar(self, datos):
        modelo = self.motivo.get(id=self.id)
        for clave in datos:
            if clave in FormularioModificar:
                if FormularioModificar[clave] == "Asunto":
                    llave = Asunto.objects.get(id=datos[clave])
                    setattr(modelo, FormularioModificar[clave], llave)
                else:
                    setattr(modelo, FormularioModificar[clave], datos[clave])
        modelo.save()
        return JsonResponse({'resultado': "Usuario Modificado"})

    def default(self, datos):
        print("Opción no válida")
        print("Estás en el caso eliminar")
        return JsonResponse({'resultado': "NOP"})

    def ejecutar_opcion(self, opcion, datos):
        metodo = getattr(self, opcion, self.default)
        return metodo(datos)
