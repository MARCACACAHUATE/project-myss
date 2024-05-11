from django.views import View
from django.shortcuts import render
# from django.contrib.auth.mixins import LoginRequiredMixin
# from propuestas.models import Propuesta


# implementar LoginRequiredMixin
class LoginView(View):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
