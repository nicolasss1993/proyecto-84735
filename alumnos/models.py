from django.db import models


class Alumnos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_de_nacimiento = models.DateField(
        blank="",
        null=True,
        default=None
    )
    nro_alumno = models.IntegerField(unique=True)
    dni = models.CharField(max_length=12, unique=True)
    email = models.CharField(max_length=50, unique=True)
    # notas = models.JsonField(...)
    def __str__(self):
        return f"Alumno({self.nro_alumno}): {self.nombre} {self.apellido} - {self.dni}"

    def ver_notas(self):
        ...
        notas = self.notas["lista_notas"]
        return notas
"""
from alumnos.models import Alumnos - Importo la tabla de la bd

Alumnos.objects.create(nombre="Fede", apellido="Perez", fecha_de_nacimiento=None, nro_alumno=2, dni="12385287", email="fede12@gmail.com")

>>> alumno = Alumnos(nombre="Nicolas", apellido="Dziuma", fecha_de_nacimiento=None, nro_alumno=1, dni="11111
111", email="nico@hotmail.es")
>>> alumno
<Alumnos: Alumno(1): Nicolas Dziuma - 11111111>
>>> alumno.save()

-----------
>>> alumno1 = Alumnos.objects.all()[0]
>>> alumno1.ver_notas()
"""