"""grand_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [

    # Home pages
    url(r'^', include('home.urls', namespace='home'), name='home'),

    # Subscriber related URLs
    url(r'^signup/', include('subscribers.urls', namespace='subscribers'), name='subscribers'),

    # Admin URL
    url(r'^admin/', admin.site.urls),

    # Login/Logout URLs


    # Account related URLs


    # Contact related URLS


    # Communication related URLs


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
