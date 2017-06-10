from django.conf.urls import url
from .views import account_detail


urlpatterns = [

    url(r'^$', account_detail, name='account_detail'),

]

