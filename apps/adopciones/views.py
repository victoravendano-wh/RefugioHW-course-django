from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from django.core.urlresolvers import reverse_lazy

# Create your views here.

from apps.adopciones.models import Solicitud, Persona
from apps.adopciones.forms import PersonaForms, SolicitudForm


class SolicitudList(ListView):
	model = Solicitud
	template_name = 'adopcion/solicitud_list.html'

class SolicitudCrear(CreateView):
	model = Solicitud
	template_name = 'adopcion/solicitud_form.html'
	form_class = SolicitudForm 
	second_form_class = PersonaForms
	success_url = reverse_lazy('app_adopciones:solicitud_listar')

	def get_context_data(self, **kwargs):
		context = super(SolicitudCrear, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class() #CHECAR ESTA PARTE, NO ME QUEDA CLARO
		if 'form2' not in context:
			context['form2'] = self.second_form_class() #ESTA PARTE IGUAL
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object  
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid():
			solicitud = form.save(commit=False)
			solicitud.persona = form2.save()
			solicitud.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))

class SolicitudUpdate(UpdateView):
	model= Solicitud
	second_model = Persona
	template_name = 'adopcion/solicitud_form.html'
	form_class = SolicitudForm
	second_form_class = PersonaForms
	success_url = reverse_lazy('app_adopciones:solicitud_listar')

	def get_context_data(self, **kwargs):
		context = super(SolicitudUpdate, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk', 0)
		solicitud = self.model.objects.get(id = pk)
		persona = solicitud.persona
		if 'form' not in context:
			context['form'] = self.form_class()
		if 'form2' not in context:
			context['form2'] = self.second_form_class(instance=persona)
		context['id'] = pk
		return context;

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		id_solicitud = kwargs['pk']
		solicitud = self.model.objects.get(id=id_solicitud)
		persona = solicitud.persona
		form = self.form_class(request.POST, instance = solicitud)
		form2 = self.second_form_class(request.POST, instance=persona)
		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())

class SolicitudEliminar(DeleteView):
	model = Solicitud
	template_name = 'adopcion/solicitud_eliminar.html'
	success_url = reverse_lazy('app_adopciones:solicitud_listar')
	 