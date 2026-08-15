from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.mascotas.forms import MascotaForm
from apps.mascotas.models import Mascota
from django.views.generic import ListViews


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

def mascota_edit(request, id_mascota):
	mascota = Mascota.objects.get(id=id_mascota) #obtenemos el objeto de la DB segun su id.
	if request.method == "GET":
		form = MascotaForm(instance=mascota) #le decimos a la view que no queremos hacer un nuevo registro, sino editar "instance" el objeto que obtuvimos con el id anteriormente
	else:
		form = MascotaForm(request.POST, instance=mascota)
		if form.is_valid():
			form.save()
		return redirect('app mascotas:lista_mascotas')
	return render(request, 'mascota/mascota_form.html', {'form':form})

def mascota_borrar(request, id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)

	if request.method == 'POST':
		mascota.delete()
		return redirect('app mascotas:lista_mascotas')

	return render(request, 'mascota/mascota_borrar.html', {'mascota':mascota})

class MascotaList(ListView):
	