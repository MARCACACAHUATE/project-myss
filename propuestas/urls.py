from django.urls import path
from propuestas.views import RevisionDocumentosView, PropuestasDetallesView


app_name = "propuestas"

urlpatterns = [
    path("", RevisionDocumentosView.as_view(), name="revision"),
    path("<int:propuesta_id>/", PropuestasDetallesView.as_view(), name="pro_detalles"),
]
