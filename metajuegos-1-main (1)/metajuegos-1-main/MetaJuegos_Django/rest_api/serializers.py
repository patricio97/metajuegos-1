from rest_framework import serializers
from core.models import Juego

class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields = ['codigoJuego','nombreJuego','genero','plataforma']