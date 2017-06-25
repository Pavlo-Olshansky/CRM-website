from django.conf.urls import url
from django.contrib import admin
from .views import HomePage, hello

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePage.as_view(), name='home'),
    url(r'^hello/(?P<uuid>[\w-]+)/', hello, name = 'hello'),


]

