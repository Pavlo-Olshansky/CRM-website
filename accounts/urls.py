from django.conf.urls import url
from .views import account_detail, account_update


urlpatterns = [

	url(r'^edit/$', account_update, name='account_update'),
	
    url(r'^$', account_detail, name='account_detail'),

]

