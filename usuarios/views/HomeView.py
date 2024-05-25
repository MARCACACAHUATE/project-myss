from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, View):
    login_url = "/login/"
    template_name = "Home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
