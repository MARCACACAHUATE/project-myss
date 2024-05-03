from django.urls import path
from propuestas.views import RevisionDocumentosView


app_name = "propuestas"

urlpatterns = [
    path("", RevisionDocumentosView.as_view(), name="revision"),
]
