from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from propuestas.forms import RechazarPropuestaForm
from propuestas.models import Propuesta
from propuestas.utils import Status
from usuarios.models import Motivo


class RechazarPropuestaView(LoginRequiredMixin, View):
    login_url = "/login"
    template_name = "rechazar_propuesta.html"

    def get(self, request, *args, **kwargs):
        form = RechazarPropuestaForm()
        motivos = Motivo.objects.all()

        context = {
            "propuesta_id": self.kwargs["propuesta_id"],
            "form": form,
            "motivos_rechazon": motivos
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        propuesta_id = self.kwargs["propuesta_id"]

        propuesta = Propuesta.objects.get(id=propuesta_id)

        form = RechazarPropuestaForm(request.POST)

        context = {
            "propuesta_id": propuesta_id,
            "form": form
        }

        if form.is_valid():
            data = form.cleaned_data
            motivo = Motivo.objects.get(Motivo=data["motivo_rechazo"])
            propuesta.descripcion_respuesta = data["descripcion"]
            propuesta.status = Status.RECHAZADA
            propuesta.motivo = motivo

            propuesta.save()

        else:
            print("Formulario Invalido")
            return render(request, self.template_name, context)

        return redirect(f"/propuestas/{propuesta_id}/")
