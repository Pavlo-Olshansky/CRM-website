from django.conf.urls import url
from .views import account_detail, account_cru, add_comment


urlpatterns = [

    url(r'^$', account_detail, name='account_detail'),
    url(r'^edit/$', account_cru, name='account_update'),
    url(r'^comment/', add_comment, name='add_comment')
]

