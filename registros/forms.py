from django import forms;
from django.forms import ModelForm, ModelChoiceField, widgets
from registros.models import Usuario
from .models import User, Profile

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
        
class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return confirm_password

class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo Electrónico', max_length=255)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude= ["estado", "user", ] 
