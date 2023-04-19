from django.shortcuts import render
from .models import Cuenta
from .forms import Cuentaform


# Create your views here.
def home(request):

    return render(request, 'core/index.html')

def login(request):

    datos= {
        'form': Cuentaform()
    }

    return render(request, 'core/login.html', datos)

def register(request):

    datos= {
        'form': Cuentaform()
    }
    if request.method== 'POST':
        formulario = Cuentaform(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Cuenta Registrada"
 
    return render(request, 'core/register.html', datos)