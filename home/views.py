from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Comment

class HomePage(TemplateView):
	"""
	We just need to assign one value; template_name.
	"""
	template_name = 'home.html'

def hello(request, uuid):
   today = datetime.datetime.now().date()
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   dreamreal = Comment.objects.get(uuid=uuid)
   return render(request, 'home.html', locals())