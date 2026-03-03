from django.urls import path
from alumnos.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("alumnos_list/", listar_alumnos, name="alumnos_list"),
    path("ver_alumno/<int:nro_alumno>/", ver_alumno, name="ver_alumno"),
]