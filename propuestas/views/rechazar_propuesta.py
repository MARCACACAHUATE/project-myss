from django.views import View
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from propuestas.forms import RechazarPropuestaForm
from propuestas.models import Propuesta
from propuestas.utils import Status


class RechazarPropuestaView(View):
    # login_url = "login"
    template_name = "rechazar_propuesta.html"

    def get(self, request, *args, **kwargs):
        print("Se esta rechazando una propuesta")

        form = RechazarPropuestaForm()

        context = {
            "propuesta_id": self.kwargs["propuesta_id"],
            "form": form
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        propuesta_id = self.kwargs["propuesta_id"]
        print(propuesta_id)

        propuesta = Propuesta.objects.get(id=propuesta_id)

        form = RechazarPropuestaForm(request.POST)

        print(form.data)

        context = {
            "propuesta_id": propuesta_id,
            "form": form
        }

        if form.is_valid():
            data = form.cleaned_data
            propuesta.descripcion_respuesta = data["descripcion"]
            propuesta.status = Status.RECHAZADA

            propuesta.save()

        else:
            print("Formulario Invalido")
            return render(request, self.template_name, context)

        return redirect(f"/propuestas/{propuesta_id}/")
