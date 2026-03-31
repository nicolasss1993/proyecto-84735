from django.urls import path
from alumnos.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("alumnos_list/", listar_alumnos, name="alumnos_list"),
    path("ver_alumno/<int:nro_alumno>/", ver_alumno, name="ver_alumno"),
    path("crear_alumno/", crear_alumno, name="crear_alumno"),
    path("actualizar_alumno/<str:dni>/", actualizar_alumno, name="actualizar_alumno"),
    path("alumno/eliminar/<str:dni>/", eliminar_alumno, name="eliminar_alumno"),
]