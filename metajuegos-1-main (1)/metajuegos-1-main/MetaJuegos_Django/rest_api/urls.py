from django.urls import path
from rest_api.views import lista_Juego, vista_juego_mod
from rest_api.viewslogin import login

urlpatterns=[
    path('lista_juego/',lista_Juego,name="lista_juego"),
    path('datos_juego/<id>',vista_juego_mod,name="modif_juego"),
    path('login/',login,name="login")
]