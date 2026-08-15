from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.mascotas.forms import MascotaForm
from apps.mascotas.models import Mascota


# Create your views here.

def mas_index(request):
	return render(request, 'mascota/mascota.html')


def mascota_view(request):
	if request.method == 'POST':
		form = MascotaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('app mascotas:mascota_index')
	else:
		form = MascotaForm()
	return render(request, 'mascota/mascota_form.html', {'form':form}) 

def mascota_list (request):
	mascota = Mascota.objects.all()
	contexto = {'mascotas':mascota}
	return render(request, 'mascota/mascota_list.html', contexto)
