from http.client import ImproperConnectionState
from django.urls import include, path
from .views import eliminar_producto, home, contacto, galeria, \
    agregar_producto, listar_productos, modificar_producto, registro, ProductoViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)


#localhost:8000/api/producto
urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro/', registro, name="registro"),
    path('api/', include(router.urls)),
]