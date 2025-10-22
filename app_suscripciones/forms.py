from django import forms
from .models import Usuario, PlanSuscripcion

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'fecha_registro', 'pais', 'plan', 'estado', 'foto_de_perfil']
        widgets = {
            'fecha_registro': forms.DateInput(attrs={'type': 'date'}),
        }

class PlanSuscripcionForm(forms.ModelForm):
    class Meta:
        model = PlanSuscripcion
        fields = ['nombre_plan', 'precio_mensual', 'dispositivos_simultaneos', 'descargas_offline', 'anuncios']