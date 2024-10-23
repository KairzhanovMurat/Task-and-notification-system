from celery import shared_task
from django.utils import timezone

from notifications.models import Notification
from tasks.models import Task


@shared_task(name='send_task_completion_notification')
def send_task_completion_notification(task_id):
    try:
        task = Task.objects.get(id=task_id)
        Notification.objects.create(
            task=task,
            message=f"Задача '{task.title}' завершена, Владелец: {task.user}"
        )
        print(f"Уведомление о завершении задачи '{task.title}' создано.")
    except Task.DoesNotExist:
        print(f"Задача с ID {task_id} не найдена.")


@shared_task(name='tasks.tasks.check_overdue_tasks')
def check_overdue_tasks():
    overdue_tasks = Task.objects.filter(due_date__lt=timezone.now(), status__in=['pending', 'in_progress'])
    for task in overdue_tasks:
        Notification.objects.create(
            task=task,
            message=f"Задача '{task.title}' просрочена!, Владелец: {task.user}",

        )
        print(f"Уведомление о просроченной задаче '{task.title}' создано.")
