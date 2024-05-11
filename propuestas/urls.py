from django.urls import path
from propuestas.views import RevisionDocumentosView, EnvioDocumentosView
from usuarios.views import LoginView
from propuestas.views import RevisionDocumentosView, PropuestasDetallesView



app_name = "propuestas"

urlpatterns = [
    path("", RevisionDocumentosView.as_view(), name="revision"),
    path("envio-propuestas/", EnvioDocumentosView.as_view(), name="formulario"),
    path("login/", LoginView.as_view(), name="login"),
    path("<int:propuesta_id>/", PropuestasDetallesView.as_view(), name="pro_detalles"),
    
]
