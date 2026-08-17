from django.conf.urls import url, include

from apps.adopciones.views import SolicitudList, SolicitudCrear, SolicitudUpdate, SolicitudEliminar


urlpatterns = [
	url(r'^solicitud/listar', SolicitudList.as_view(), name='solicitud_listar'),
	url(r'^solicitud/crear', SolicitudCrear.as_view(), name='solicitud_crear'),
    url(r"^solicitud/editar/(?P<pk>\d+)$", SolicitudUpdate.as_view(), name="solicitud_actualizar"),
	url(r'^solicitud/eliminar/(?P<pk>\d+)$', SolicitudEliminar.as_view(), name="solicitudBorrar")
]