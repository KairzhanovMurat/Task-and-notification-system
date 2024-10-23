import pytest
from django.utils import timezone
from tasks.tasks import check_overdue_tasks, send_task_completion_notification
from notifications.models import Notification
from ..factories import TaskFactory

pytestmark = [pytest.mark.django_db]


class TestNotifications:

    def test_check_overdue_tasks(self, celery_app):
        overdue_task = TaskFactory(due_date=timezone.now() - timezone.timedelta(days=1), status='pending')
        check_overdue_tasks.delay()
        notification = Notification.objects.filter(task=overdue_task).first()
        assert notification is not None
        assert notification.message == f"Задача '{overdue_task.title}' просрочена!, Владелец: {overdue_task.user}"

    def test_task_completed_notification(self, authenticated_client, task, celery_app):
        url = f'/api/tasks/{task.id}/'
        data = {'status': 'completed'}
        authenticated_client.patch(url, data)
        send_task_completion_notification.delay(task.id)
        notification = Notification.objects.filter(task=task).first()
        assert notification.message == f"Задача '{task.title}' завершена, Владелец: {task.user}"
