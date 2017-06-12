from django.conf.urls import url
from .views import contacts_detail


urlpatterns = [

    url(r'^$', contacts_detail, name='contacts_detail'),

]
