from django.conf import settings
import django
import os
def before_all(context):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'auth.settings'
    if not settings.configured:
        django.setup()