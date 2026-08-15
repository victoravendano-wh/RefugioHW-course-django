from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.mascotas.forms import MascotaForm


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