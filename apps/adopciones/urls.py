from django.conf.urls import url, include

from apps.adopciones.views import index

urlpatterns = [

	url(r'^$', index)

]