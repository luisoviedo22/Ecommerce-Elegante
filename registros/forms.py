from django import forms;
from django.forms import ModelForm, ModelChoiceField, widgets
from registros.models import Usuario

class UsuarioForm(ModelForm):
    
    class Meta:
        model= Usuario
        fields= "__all__"
        exclude= ["estado", "user"]
        widgets={
            'fecha_nacimiento':widgets.DateInput(attrs={'type':'date'}, format='%Y-%m-%d')
        }

class UsuarioEditarForm(ModelForm):
    
    class Meta:
        model= Usuario
        fields= "__all__"
        exclude= ["estado", "user", "documento", "fecha_nacimiento"]
        