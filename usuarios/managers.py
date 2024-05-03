from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from usuarios.models import Role


class CustomUserManager(BaseUserManager):

    def create_user(self, num_empleado, nombre, password, **extra_fields):
        """
        Crea un usuario con el nombre, numero de empleado y password.
        """
        if not num_empleado:
            raise ValueError(_("El usuario debe tener un numero de empleado"))

        if extra_fields.get("is_superuser"):
            role, created = Role.objects.get_or_create(nombre_role="Admin")
        else:
            role, created = Role.objects.get_or_create(nombre_role="Analista")

        user = self.model(numero_empleado=num_empleado,
                          nombre=nombre)
        user.set_password(password)
        user.role_id = role
        user.save()
        return user

    def create_superuser(self, numero_empleado, nombre, password, **extra_fields):
        """
        Crea un SuperUsuario con el nombre, numero de empleado y password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(numero_empleado, nombre, password, **extra_fields)
