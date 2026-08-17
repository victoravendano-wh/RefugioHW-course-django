from django.conf.urls import url, include

from apps.adopciones.views import SolicitudList, SolicitudCrear

urlpatterns = [
	url(r'^solicitud/listar', SolicitudList.as_view(), name='solicitud_listar'),
	url(r'^solicitud/crear', SolicitudCrear.as_view(), name='solicitud_crear')
]