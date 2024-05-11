from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def login_user(request):

    if request.method == 'POST':
        matricula = request.POST["matricula"]
        password = request.POST["password"]
        user = authenticate(request, matricula=matricula, password=password)

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