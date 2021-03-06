import os
from celery import Celery
from django.conf import settings

from datetime import datetime, timedelta
from celery.task import periodic_task

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "metameme.settings")

app = Celery('metameme')

CELERY_TIMEZONE = 'UTC'

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
