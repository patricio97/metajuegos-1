from django import forms
from django.forms import ModelForm
from .models import Credencial

class CredencialForm(ModelForm):
    class Meta:
        model = Credencial
        fields =['username','password']

        widget = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.TextInput(attrs={'class':'form-control'}),
        }