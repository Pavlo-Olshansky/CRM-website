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
from django.contrib.auth import views as auth_views
from accounts.views import AccountList
from accounts import views as accounts_views
from contacts import views as contacts_views
from contacts.views import ContactDelete


admin.autodiscover()

urlpatterns = [

    # Home pages
    url(r'^', 
        include('home.urls', namespace='home'), name='home'),

    # Subscriber related URLs
    url(r'^signup/', 
        include('subscribers.urls', namespace='subscribers'), name='subscribers'),

    # Admin URL
    url(r'^admin/', 
        admin.site.urls),

    # Login/Logout URLs
    url(r'^login/$',
        auth_views.login, {'template_name': 'login.html'}, name='login'
    ),

    url(r'^logout/$',
        auth_views.logout, {'next_page': '/login/'}, name='logout'
    ),

    # Account related URLs
    url(r'^account/new/$', 
        accounts_views.account_cru, name='account_new'),

    url(r'^account/list/$',
        AccountList.as_view(), name='account_list'),

    url(r'^account/(?P<uuid>[\w-]+)/', 
        include('accounts.urls')),

    # Contact related URLS
    url(r'^contact/new/$', 
       contacts_views.contact_cru, name='contact_new'),

    url(r'^contacts/(?P<uuid>[\w-]+)/', 
        include('contacts.urls')),

    url(r'^contact/(?P<pk>[\w-]+)/delete/$',
        ContactDelete.as_view(), name='contact_delete'),

    # Communication related URLs
    url(r'^comm/(?P<uuid>[\w-]+)/', 
        include('communications.urls')),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
