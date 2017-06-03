from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePage(TemplateView):
	"""
	We just need to assign one value; template_name.
	"""
	template_name = 'home.html'