from django.urls import path
from.views import home
from . import views

urlpatterns = [
    path('', home, name="home"),
    path('home', views.home, name="home"),
    path('login-app', views.login,name="login_app"),
    path('register-app', views.register,name="register_app"),
    path('carrito-app', views.carrito,name="carrito_app"),
]