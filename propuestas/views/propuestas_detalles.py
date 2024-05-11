from django.views import View
from django.shortcuts import render
# from django.contrib.auth.mixins import LoginRequiredMixin
from propuestas.models import Propuesta


class PropuestasDetallesView(View):
    template_name = "propuesta_detalles.html"

    def get(self, request, *args, **kwargs):
        id = self.kwargs['propuesta_id']
        print(f"Detalles de la propuesta {id}")

        propuesta = Propuesta.objects.get(id=id)
        print(propuesta)
        return render(request, self.template_name, {"propuesta_data": propuesta})
