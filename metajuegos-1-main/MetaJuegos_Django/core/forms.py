from django import forms
from django.forms import ModelForm
from .models import Cuenta


class Cuentaform(ModelForm):
    class Meta:
        model = Cuenta
        fields= ['username','password']

        widget = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.TextInput(attrs={'class':'form-control'}),
        }