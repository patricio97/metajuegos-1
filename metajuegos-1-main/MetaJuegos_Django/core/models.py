from django.db import models

# Create your models here.   
class Juego(models.Model):
    codigoJuego = models.IntegerField(verbose_name="Id Juego")
    nombreJuego = models.CharField(max_length=60, verbose_name="Nombre Juego")
    genero = models.IntegerField(verbose_name="Genero Juego")
    plataforma = models.IntegerField(verbose_name="Plataforma")

    def __int__(self):
        return self.codigoJuego
    
class Carrito(models.Model):
    idCarrito = models.IntegerField(primary_key=True, verbose_name="Id Carrito")

    def __str__(self):
        return self.idCarrito
  
    