from django.conf.urls import url, include
from django.contrib import admin
from . import views


# app_name = 'grand_site_1'
urlpatterns = [
    url(r'^$', views.subscriber_new, name='sub_new'),

]
