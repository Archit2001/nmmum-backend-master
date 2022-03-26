from __future__ import absolute_import, unicode_literals
from datetime import timezone
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('backend')
app.conf.enable_utc = False

app.conf.update(timezone='Asia/Kolkata')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery Beat Settings

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Hello from dalal')


@app.task
def print_hello():
    print("helllo billo")


