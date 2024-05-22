from datetime import datetime
from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from propuestas.models import Propuesta


class RevisionDocumentosView(LoginRequiredMixin, View):
    login_url = "/login"
    template_name = "revision_home.html"

    def get(self, request, *args, **kwargs):

        filter = request.GET.get("filter", "todo")
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        if start_date and end_date:
            try:
                start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
                end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            except ValueError:
                start_date = end_date = None
        else:
            start_date = end_date = None

        if filter == "aceptadas":
            if start_date is None or end_date is None:
                propuestas = Propuesta.objects.filter(
                    status="Aceptada"
                )
            else:
                propuestas = Propuesta.objects.filter(
                    status="Aceptada",
                    fecha_creacion__gte=start_date,
                    fecha_creacion__lte=end_date
                )

        elif filter == "rechazadas":
            if start_date is None or end_date is None:
                propuestas = Propuesta.objects.filter(
                    status="Rechazada"
                )
            else:
                propuestas = Propuesta.objects.filter(
                    status="Rechazada",
                    fecha_creacion__gte=start_date,
                    fecha_creacion__lte=end_date
                )

        else:
            if start_date is None or end_date is None:
                propuestas = Propuesta.objects.all()
            else:
                propuestas = Propuesta.objects.filter(
                    fecha_creacion__gte=start_date,
                    fecha_creacion__lte=end_date
                )

        context = {
            "lista_propuestas": propuestas,
            "filter": filter,
            "start_date": start_date,
            "end_date": end_date,
        }

        return render(request, self.template_name, context)
