from rest_framework import serializers
from core.models import Mascota

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ['codigoChip','nombreMascota','edadMascota','raza']