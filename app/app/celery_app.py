import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app')

# Read celery settings from Django's settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover tasks from all installed apps
app.autodiscover_tasks()

# Define periodic tasks here
app.conf.beat_schedule = {
    'print-hello-every-10-seconds': {
        'task': 'core.tasks.say_hello',
        'schedule': 10.0,  # seconds
    },
    'print-time-every-minute': {
        'task': 'core.tasks.print_time',
        'schedule': crontab(minute='*'),
    }
}