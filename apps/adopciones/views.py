from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from django.core.urlresolvers import reverse_lazy

# Create your views here.

from apps.adopciones.models import Solicitud
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
			context['form'] = self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.GET)
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