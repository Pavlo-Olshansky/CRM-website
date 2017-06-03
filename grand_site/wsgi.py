"""
WSGI config for grand_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crmapp.settings")

# # from django.core.wsgi import get_wsgi_application

# # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "grand_site.settings")

# # application = get_wsgi_application()

# from django.core.wsgi import get_wsgi_application
# from dj_static import Cling

# application = Cling(get_wsgi_application())

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "grand_site.settings")

application = get_wsgi_application()
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
