from django.contrib import admin

# Register your models here.
from .models import Categoria
admin.site.register(Categoria)

from .models import Producto
admin.site.register(Producto)

from .models import Compra
admin.site.register(Compra)

from .models import DetalleCompra
admin.site.register(DetalleCompra)

admin.site.site_header = 'Django Test Admin'
admin.site.site_title = 'Contenido'
admin.site.index_title = 'Administración'