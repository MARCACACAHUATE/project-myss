from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


@method_decorator(cache_page(60 * 15), name='dispatch')
class HomeView(LoginRequiredMixin, View):
    login_url = "/login/"
    template_name = "Home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
