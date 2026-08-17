from django.conf.urls import url, include

from apps.mascotas.views import mas_index, mascota_view, mascota_list, mascota_edit, mascota_borrar 
from apps.mascotas.views import MascotaList, MascotaCrear, MascotaUpdate, MascotaEliminar



urlpatterns = [

	url(r'^$', mas_index, name='mascota_index'),
	url(r'^nuevo$', MascotaCrear.as_view(), name='mascota_crear'),
	url(r'^listar$', MascotaList.as_view(), name='lista_mascotas' ),
    url(r'^editar/(?P<pk>\d+)$', MascotaUpdate.as_view(), name='edicion_mascotas'), #vistas genericas estan buscando 'pk' -pimary key, la pasamos en URL params
    url(r'^borrar/(?P<pk>\d+)$', MascotaEliminar.as_view(), name='borrar_mascota')

]
