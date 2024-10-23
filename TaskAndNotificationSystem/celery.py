import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TaskAndNotificationSystem.settings')

app = Celery('TaskAndNotificationSystem')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check_overdue_tasks': {
        'task': 'tasks.tasks.check_overdue_tasks',
        'schedule': crontab(hour='*', minute='0'),
    }
}
