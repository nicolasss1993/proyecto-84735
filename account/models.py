from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import uuid

def get_code():
    return uuid.uuid4().hex # h1234h12h-1lhfl3113-hghlñiahkk-ljf31231


def avatar_upload_to(instance, filename):
    return f"avatars/{instance.username}/{filename}"


def get_user_number():
    number = random.randint(0, 10000000)
    for i in range(10):
        perfil = Perfil.objects.filter(nro_usuario=number)
        if perfil.exists():
            number = random.randint(0, 10000000)
        else:
            return number


class Perfil(AbstractUser):
    avatar = models.ImageField(
        upload_to=avatar_upload_to,
        default="default/default.png",
        blank=True,
        null=True,
        verbose_name="Avatar"
    )
    pais = models.CharField(max_length=50)
    dni = models.CharField(max_length=12)
    direccion = models.CharField(max_length=100)
    nro_usuario = models.IntegerField(unique=True, default=get_user_number)
    # code = models.CharField(max_length=32, unique=True)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

    def __str__(self):
        return f"Perfil: {self.email} - {self.first_name}, {self.last_name} / Nro: {self.nro_usuario}"
