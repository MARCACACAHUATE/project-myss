from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from propuestas.models import Propuesta


class RevisionDocumentosView(LoginRequiredMixin, View):
    login_url = "/login"
    template_name = "revision_home.html"

    def get(self, request, *args, **kwargs):
        propuestas = Propuesta.objects.all()
        for pro in propuestas:
            print(pro.nombre)

        return render(request, self.template_name, {"lista_propuestas": propuestas})
