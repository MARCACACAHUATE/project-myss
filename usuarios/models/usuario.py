from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from usuarios.managers import CustomUserManager


class Usuario(AbstractBaseUser, PermissionsMixin):
    numero_empleado = models.CharField(max_length=8, unique=True)
    nombre = models.CharField(max_length=100)
    departamento = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    password = models.TextField()
    role_id = models.ForeignKey("Role", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    cerated_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(null=True)

    USERNAME_FIELD = "numero_empleado"
    REQUIRED_FIELDS = ["nombre"]

    objects = CustomUserManager()

    def __str__(self):
        return self.nombre
