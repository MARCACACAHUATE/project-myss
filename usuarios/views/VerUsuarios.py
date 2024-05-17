from django.views import View
from django.shortcuts import render, redirect
from usuarios.models import Usuario
import json
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
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
            if Duplicado(Numero):
                print("what")
                # Faltaria poner alerta de error
                return HttpResponseRedirect(reverse('usuarios:usuarios'))
            else:
                print("where")
                usuario = Usuario.objects
                usuario.create_user(Numero, Nombre, Contraseña)
                return HttpResponseRedirect(reverse('usuarios:usuarios'))


def RespuestaAJAX(request):
    datos = json.loads(request.body)
    try:
        Accion = datos.get("Accion")
        Usuario = datos.get("Usuario")
        switch = Acciones_Usuario(datos.get("Usuario"))

    except Exception as e:
        # Manejo de la excepción
        return JsonResponse({'error': str(e)}, status=500)
        # Numero = request.POST['numero_empleado']
        # Contraseña = request.POST['Contraseña']
        # Accion = request.POST['Accion']
        # Correo = request.POST['Correo']
    # usuario.create_user(Numero, Nombre, Contraseña)
    if Duplicado(Usuario):
        return JsonResponse({'resultado': "Usuario found" + Usuario})
    else:
        print(datos)
        return switch.ejecutar_opcion(Accion, datos)


def Duplicado(ID):
    try:
        ultimo_objeto = Usuario.objects.get(numero_empleado=ID)
        return True
    except ObjectDoesNotExist:
        return False


"""numero_empleado = models.CharField(max_length=8, unique=True)
nombre = models.CharField(max_length=100)
departamento = models.CharField(max_length=50)
correo = models.EmailField()
password = models.TextField()
role_id = models.ForeignKey("Role", on_delete=models.CASCADE)
is_active = models.BooleanField(default=True)
is_staff = models.BooleanField(default=False)
cerated_at = models.DateTimeField(default=timezone.now)
modified_at = models.DateTimeField(null=True)"""

FormularioModificar = {"m_Nombre": "nombre",
                       "m_numero_empleado": "numero_empleado", "m_role": "role_id", "m_Contraseña": "password"}


class Acciones_Usuario:
    def __init__(self, id):
        self.id = id
        self.usuario = Usuario.objects

    def Eliminar(self, datos):
        objeto_a_modificar = self.usuario.get(id=self.id)
        objeto_a_modificar.delete()
        return JsonResponse({'resultado': "SIP"})

    def Bloquear(self, datos):
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

    def Desbloquear(self, datos):
        objeto_a_modificar = self.usuario.get(id=self.id)
        objeto_a_modificar.is_active = True
        print(objeto_a_modificar.password)
        objeto_a_modificar.save()
        return JsonResponse({'resultado': "Usuario Deshabilitado"})

    def Modificar(self, datos):
        modelo = self.usuario.get(id=self.id)
        for clave in datos:
            if clave in FormularioModificar:
                if FormularioModificar[clave] == "password":
                    modelo.set_password(datos[clave])
                else:
                    setattr(modelo, FormularioModificar[clave], datos[clave])
        modelo.modified_at = datetime.now()
        modelo.save()
        return JsonResponse({'resultado': "Usuario Modificado"})
#           objeto_a_modificar = self.usuario.get(id=self.id)
 # 3        objeto_a_modificar.save()

    def default(self, datos):
        print("Opción no válida")
        print("Estás en el caso eliminar")
        return JsonResponse({'resultado': "NOP"})

    def ejecutar_opcion(self, opcion, datos):
        metodo = getattr(self, opcion, self.default)
        return metodo(datos)
