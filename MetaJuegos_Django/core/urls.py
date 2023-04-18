from django.urls import path
from .views import home, login, register

urlpatterns = [
    path('', home, name="home"),
    path('login-app', login, name="login"),
    path('register-app', register, name="register"),
]