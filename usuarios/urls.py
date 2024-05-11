from django.urls import path
from usuarios.views import LoginView


app_name = "propuestas"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
]
