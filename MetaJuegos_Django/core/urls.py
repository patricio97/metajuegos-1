from django.urls import path
from .views import home, login, register

urlpatterns = [
    path('', home, name="home"),
    path('home', home, name="home"),
    path('login-app', login,name="login_app"),
    path('register-app', register,name="register_app"),
]