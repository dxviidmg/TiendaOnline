from django.contrib import admin
from .models import *

class ProductoAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("nombre",)}

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
# Register your models here.
