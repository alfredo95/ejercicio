from django.contrib import admin

from catalogo.models import Producto, Inventario

#

admin.site.register(Producto)
admin.site.register(Inventario)
