"""
WSGI config for mood_tracker project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mood_tracker.settings")

from whitenoise import WhiteNoise

application = WhiteNoise(get_wsgi_application(), root=os.environ["STATIC_ROOT"])
