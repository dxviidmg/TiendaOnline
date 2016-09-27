from django.shortcuts import render
from django.views.generic import View

class Home(View):
	def get(self, request):
		template_name = 'main/index.html'
		return render(request, template_name)

class Nosotros(View):
	def get(self, request):
		template_name = 'main/nosotros.html'
		return render(request, template_name)

class Contacto(View):
	def get(self, request):
		template_name = 'main/contacto.html'
		return render(request, template_name)