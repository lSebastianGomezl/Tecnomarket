from django.contrib import admin
from .models import Contacto, Marca, Producto
from .forms import ProductoForm
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio","nuevo","marca"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter =["marca","nuevo"]
    list_per_page = 5
    form = ProductoForm



admin.site.register(Marca)
admin.site.register(Producto, ProductAdmin)
admin.site.register(Contacto)