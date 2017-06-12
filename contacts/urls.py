from django.conf.urls import url
from .views import contact_detail


urlpatterns = [

    url(r'^$', contact_detail, name='contact_detail'),

]
