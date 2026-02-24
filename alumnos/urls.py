from django.urls import path
from alumnos.views import *

urlpatterns = [
    path("", inicio, name="inicio")
]