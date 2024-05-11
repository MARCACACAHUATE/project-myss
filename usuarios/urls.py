from django.urls import path
from usuarios.views import *


app_name = "usuarios"

urlpatterns = [
    path("login", LoginView.as_view(), name="login"),
    path("C", CorreoPlantilla.as_view(), name="correo"),
    path("PlantillaMail", Plantilla_Mail.as_view(), name="correobase"),
    path("", Ver_Usuarios.as_view(), name="usuarios"),
    path("NuevoUsuario", Crear_Usuarios.as_view(), name="NuevoUsuario"),
    path("Asuntos", Ver_Asuntos.as_view(), name="VerAsunto"),
    path("NuevoAsunto", Crear_Asunto.as_view(), name="CrearAsunto"),
    path("Motivos", Ver_Motivo.as_view(), name="VerMotivo"),
    path("NuevoMotivo", Crear_Motivo.as_view(), name="CrearMotivo"),
]
