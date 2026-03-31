from django.urls import path
from profesores.views import *

urlpatterns = [
    path("", ProfesoresListView.as_view(), name="profesores_list"),
    path("crear/", ProfesoresCreateView.as_view(), name="profesores_create"),
    path("<int:nro_legajo>/actualizar/", ProfesoresUpdateView.as_view(), name="profesores_update"),
    path("<int:nro_legajo>/eliminar/", ProfesoresDeleteView.as_view(), name="profesores_delete"),
    path("<int:nro_legajo>/ver/", ProfesoresDetailView.as_view(), name="profesor_detail"),
]