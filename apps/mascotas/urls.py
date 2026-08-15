from django.conf.urls import url, include

from apps.mascotas.views import mas_index, mascota_view, mascota_list, mascota_edit, mascota_borrar



urlpatterns = [

	url(r'^$', mas_index, name='mascota_index'),
	url(r'^nuevo$', mascota_view, name='mascota_crear'),
	url(r'^listar$', mascota_list, name='lista_mascotas' ),
    url(r'^editar/(?P<id_mascota>\d+)$', mascota_edit, name='edicion_mascotas'),
    url(r'^borrar/(?P<id_mascota>\d+)$', mascota_borrar, name='borrar_mascota')

]
