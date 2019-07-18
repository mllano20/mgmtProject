from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    Usuario = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Contrasena = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
