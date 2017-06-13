from django.conf.urls import url
from .views import comm_detail, comm_cru

urlpatterns = [

	url(r'^$', comm_detail, name="comm_detail"),

    url(r'^edit/$', comm_cru, name='comm_update'),
	
]