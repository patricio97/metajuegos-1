from django.shortcuts import render
        
# Create your views here.
def home(request):

    return render(request, 'core/home.html')

def login(request):

    return render(request, "core/login.html")

def register(request):

    return render(request, "core/register.html")

def carrito(request):

    return render(request, "core/carrito.html")