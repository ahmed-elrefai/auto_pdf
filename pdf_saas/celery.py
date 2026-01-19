import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pdf_saas.settings')

app = Celery('pdf_saas')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()