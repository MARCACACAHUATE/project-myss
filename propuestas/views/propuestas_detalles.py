from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from propuestas.models import Propuesta
from propuestas.utils import Status


class PropuestasDetallesView(LoginRequiredMixin, View):
    login_url = "/login"
    template_name = "propuesta_detalles.html"

    def get(self, request, *args, **kwargs):
        id = self.kwargs['propuesta_id']
        print(f"Detalles de la propuesta {id}")

        propuesta = Propuesta.objects.get(id=id)
        print(propuesta)
        return render(request, self.template_name, {"propuesta_data": propuesta})

    def post(self, request, *args, **kwargs):
        id = self.kwargs['propuesta_id']

        propuesta = Propuesta.objects.get(id=id)
        propuesta.status = Status.ACEPTADA
        propuesta.save()

        return render(request, self.template_name, {"propuesta_data": propuesta})
