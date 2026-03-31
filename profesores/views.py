from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    CreateView,
    UpdateView
)
from profesores.models import Profesores


class ProfesoresListView(ListView):
    model = Profesores
    template_name = "profesores/profes_list.html"
    context_object_name = "profesores_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        nombre = self.request.GET.get("nombre")
        if nombre not in ["", None, " "]:
            return queryset.filter(nombre__icontains=nombre).order_by("-nombre")
        return queryset


class ProfesoresDetailView(DetailView):
    model = Profesores
    template_name = "profesores/profes_detail.html"
    context_object_name = "profesor"
    slug_field = "nro_legajo"
    slug_url_kwarg = "nro_legajo"
    

class ProfesoresDeleteView(DeleteView):
    model = Profesores
    template_name = "profesores/profes_confirm_delete.html"
    success_url = reverse_lazy("profesores_list")


class ProfesoresUpdateView(UpdateView):
    model = Profesores
    fields = ["nombre", "apellido"]
    slug_field = "nro_legajo"
    slug_url_kwarg = "nro_legajo"
    success_url = reverse_lazy("profesores_list")


class ProfesoresCreateView(CreateView):
    model = Profesores
    template_name = "profesores/profes_form.html"
    fields = ["nombre", "apellido", "nro_legajo", "email", "fecha_de_ingreso"]
    
    # def get_success_url(self):
    #     return reverse_lazy(
    #         "profesor_detail",
    #         kwargs={"nro_legajo": self.object.nro_legajo}
    #     )