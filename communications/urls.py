from django.conf.urls import url
from .views import comm_detail

urlpatterns = [

	url(r'^$', comm_detail, name="comm_detail"),
	
]