from django.shortcuts import render
import requests
from datetime import datetime
import pytz
        
# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def login(request):
    return render(request, "core/login.html")

def register(request):
    return render(request, "core/register.html")

def carrito(request):
    return render(request, "core/carrito.html")

def obtener_tipo_cambio():
    url = "https://api.apilayer.com/exchangerates_data/convert"
    headers = {"apikey": "PTDPbjtjEFQljw0w20FCeGbHnKNY5e0k"}
    parametros = {"from": "USD", "to": "CLP", "amount": 1}
    
    response = requests.get(url, headers=headers, params=parametros)
    
    if response.status_code == 200:
        tipo_cambio = response.json()["result"]
    else:
        tipo_cambio = "Error al obtener el tipo de cambio"
    
    return tipo_cambio

def index(request):
    tipo_cambio = obtener_tipo_cambio()
    return render(request, "core/index.html", {"tipo_cambio": tipo_cambio})

def obtener_clima(ciudad):
    api_key = "3dc41b1f91027914804e7e5439a814ba"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperatura = data["main"]["temp"]
        tiempo_unix = data["dt"]
        zona_horaria = data["timezone"]
        print(f"Temperatura: {temperatura}, Tiempo UNIX: {tiempo_unix}, Zona horaria: {zona_horaria}")  # Mensaje de depuración
        return temperatura, tiempo_unix, zona_horaria
    else:
        print(f"Error al obtener datos de la API de OpenWeatherMap. Código de estado: {response.status_code}")  # Mensaje de depuración
        return None, None, None

def convertir_unix_a_hora(tiempo_unix, zona_horaria):
    if tiempo_unix is not None and zona_horaria is not None:
        hora_local = datetime.utcfromtimestamp(tiempo_unix + zona_horaria)
        return hora_local.strftime('%Y-%m-%d %H:%M:%S')
    else:
        return None

def index(request):
    ciudad = "Santiago,cl"  # Reemplaza con la ciudad deseada
    temperatura, tiempo_unix, zona_horaria = obtener_clima(ciudad)
    hora_local = convertir_unix_a_hora(tiempo_unix, zona_horaria)
    tipo_cambio = obtener_tipo_cambio()
    
    context = {
        "temperatura": temperatura,
        "hora_local": hora_local,
        "tipo_cambio": tipo_cambio
    }
    
    return render(request, "core/home.html", context)