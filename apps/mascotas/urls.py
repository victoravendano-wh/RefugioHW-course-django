from django.conf.urls import url, include

from apps.mascotas.views import mas_index

urlpatterns = [

	url(r'^$', mas_index)

]