from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
# from django.contrib.auth.mixins import LoginRequiredMixin
# from propuestas.models import Propuesta


# implementar LoginRequiredMixin
class LoginView(View):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


    def login_user(request):

        if request.method == 'POST':
            numero_empleado = request.POST["numero_empleado"]
            password = request.POST["password"]
            user = authenticate(request, numero_empleado=numero_empleado, password=password)

            if user is not None:
                    request.session["role"] = user.role_id.Role
                    request.session["user_id"] = user.id

                    login(request, user)
                    return redirect("/")
            else:
                return render(request, "login.html", {
                    "mensaje": "Credenciales invalidas"
                })

        return render(request, "login.html")


    def logout_user(request):
        logout(request)
        return redirect("/login/")