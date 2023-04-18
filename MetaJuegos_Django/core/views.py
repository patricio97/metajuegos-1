from django.shortcuts import render
from .models import Credencial, Producto
from .forms import CredencialForm

# Create your views here.
def home(request):
    
    Productos = Producto.objects.all()
    contexto ={"Productos":Productos}

    return render(request, 'core/index.html', contexto)

def login(request):

    return render(request, 'core/login.html')

def register(request):
    datos= {
        'form': CredencialForm()
    }
    
    return render(request, 'core/register.html', datos)