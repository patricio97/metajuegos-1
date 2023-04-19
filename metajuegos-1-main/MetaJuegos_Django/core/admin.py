from django.contrib import admin
from .models import Credencial, Usuario, Producto, Carrito, Cuenta

# Register your models here.
admin.site.register(Credencial)
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(Cuenta)
