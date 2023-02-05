from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar

class CreateArticulo(forms.Form):
    titulo = forms.CharField(label="Titulo del articulo", max_length=200)
    subtitulo = forms.CharField(label="Subtitulo del articulo", max_length=200)
    cuerpo = forms.CharField(label="Cuerpo del articulo", widget=forms.Textarea)

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar 
        fields = ["imagen"]       


"""
class ImagenFormulario(forms.ModelForm):

    class Meta:
        model = Imagen 
        fields = ["imagen"]               
"""
