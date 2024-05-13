from django.views import View
from django.shortcuts import render
from django.conf import settings
import os
from django.utils.datastructures import MultiValueDictKeyError
from propuestas.models import Propuesta, TipoPropuesta
from usuarios.models import Usuario
from django.core.exceptions import ObjectDoesNotExist


# from django.contrib.auth.mixins import LoginRequiredMixin
# from propuestas.models import Propuesta


# implementar LoginRequiredMixin
class EnvioDocumentosView(View):
    template_name = "formulario_propuestas.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        try:
            ultimo_objeto = Propuesta.objects.latest('id')
            ultimo_id = ultimo_objeto.id
            ultimo_id += 1
        except ObjectDoesNotExist:
            ultimo_id = 1
        ultimo_user = Usuario.objects.latest('id')
        user = ultimo_user.id
        nombre_archivo = str(ultimo_id) + ".pdf"
        tipo, created = TipoPropuesta.objects.get_or_create(
            nombre_tipo="Infraestructura")
        tipo.save()
        no_empleado = request.POST['numero_empleado']
        nombre_empleado = request.POST['nombre_empleado']
        telefono_contacto = request.POST['telefono_contacto']
        torre = request.POST['torre']
        area = request.POST['area']
        puesto = request.POST['puesto']
        correo_personal = request.POST['correo_personal']
        Propuesta.objects.create(
            nombre=nombre_empleado,
            no_empleado=no_empleado,
            correo=correo_personal,
            area=area,
            puesto=puesto,
            correo_personal=correo_personal,
            telefono=telefono_contacto,
            torre_perteneciente=torre,
            tipo_propuesta_id_id=tipo.id,
            supervisor_id_id=ultimo_user.id,  # Observa que el campo se llama supervisor_id_id
            # Observa que el campo se llama tipo_propuesta_id_
            status='PENDIENTE',  # Valor por defecto para el campo status
            descripcion_respuesta='',  # Valor por defecto para el campo descripcion_respuesta
            # Valor por defecto para el campo archivo_propuesta
            archivo_propuesta=nombre_archivo
        )
        # Resto del código para manejar el archivo
        try:
            archivo = request.FILES['documento']
            print("SSSSSSIo se encontró el campo 'documento' en request.FILES")
            ruta = handle_uploaded_file(archivo, nombre_archivo)
            # Resto del código para manejar el archivo
        except MultiValueDictKeyError:
            print("No se encontró el campo 'documento' en request.FILES")
            # Manejar el error de alguna manera, por ejemplo, redirigir a una página de error
        return render(request, self.template_name)


def handle_uploaded_file(archivo, nombre):
    upload_folder = os.path.join(
        settings.MEDIA_ROOT, 'theme/static')
    # Verifica si la carpeta de carga existe, si no, la crea
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    with open(os.path.join(upload_folder, nombre), 'wb+') as destination:
        for chunk in archivo.chunks():
            destination.write(chunk)
    return archivo.name
