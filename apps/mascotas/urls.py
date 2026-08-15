from django.conf.urls import url, include

from apps.mascotas.views import mas_index, mascota_view



urlpatterns = [

	url(r'^$', mas_index, name='mascota_index'),
	url(r'^nuevo$', mascota_view, name='mascota_crear')


]
