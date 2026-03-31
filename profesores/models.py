from django.db import models


class Profesores(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=50)
    nro_legajo = models.IntegerField(unique=True)
    fecha_de_ingreso = models.DateField(auto_now_add=True)
    email = models.EmailField()

    def __str__(self):
        return f"Profesor: {self.nombre} - {self.apellido} / Legajo: {self.nro_legajo}"

