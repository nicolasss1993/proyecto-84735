from django.contrib import admin
from alumnos.models import Alumnos


# admin.site.register(Alumnos)

@admin.register(Alumnos)
class AlumnoAdmin(admin.ModelAdmin):
    # Columnas visibles en la lista del modelo
    list_display = ("nombre", "apellido", "nro_alumno", "dni")
    # Columnas con enlaces clickeables para entrar al detalle
    list_display_links = ("nombre",)
    # Campos por los que buscar los registros
    search_fields = ("dni",)
    # Filtros laterlares
    list_filter = ("fecha_de_nacimiento",)
    # Orden por defecto
    ordering = ("nro_alumno", "nombre")
    # Campos que no se pueden modificar
    readonly_fields = ("nro_alumno",)
