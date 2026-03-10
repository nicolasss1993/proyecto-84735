from django import forms
from .models import Alumnos
#from alumnos.models import Alumnos


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ["nombre", "apellido", "fecha_de_nacimiento", "dni", "email", "nro_alumno"]
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "nro_alumno": forms.NumberInput(attrs={'class': 'form-control'}),
            "apellido": forms.TextInput(attrs={'class': 'form-control'}),
            "fecha_de_nacimiento": forms.DateInput(attrs={'class': 'form-control'}),
            "dni": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'})
        }
