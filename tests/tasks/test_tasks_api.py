import pytest
from django.utils import timezone
from rest_framework import status

from tasks.models import Task

pytestmark = [pytest.mark.django_db]


class TestTasksApi:
    def test_list_tasks(self, authenticated_client, task):
        url = '/api/tasks/'
        response = authenticated_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data[0]['title'] == task.title

    def test_retrieve_task(self, authenticated_client, task):
        url = f'/api/tasks/{task.id}/'
        response = authenticated_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == task.title

    def test_create_task(self, authenticated_client, user):
        url = '/api/tasks/'
        data = {
            'title': 'New Task',
            'description': 'Test task description',
            'status': 'pending',
            'due_date': timezone.now().isoformat()
        }
        response = authenticated_client.post(url, data)

        assert response.status_code == status.HTTP_201_CREATED
        assert Task.objects.count() == 1
        assert Task.objects.first().title == 'New Task'

    def test_update_task(self, authenticated_client, task):
        url = f'/api/tasks/{task.id}/'
        data = {
            'title': 'Updated Task',
            'description': task.description,
            'status': 'in_progress',
            'due_date': task.due_date.isoformat()
        }
        response = authenticated_client.put(url, data)

        assert response.status_code == status.HTTP_200_OK
        task.refresh_from_db()
        assert task.title == 'Updated Task'
        assert task.status == 'in_progress'

    def test_partial_update_task(self, authenticated_client, task):
        url = f'/api/tasks/{task.id}/'
        data = {'title': 'Partially Updated Task'}
        response = authenticated_client.patch(url, data)

        assert response.status_code == status.HTTP_200_OK
        task.refresh_from_db()
        assert task.title == 'Partially Updated Task'

    def test_delete_task(self, authenticated_client, task):
        url = f'/api/tasks/{task.id}/'
        response = authenticated_client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Task.objects.count() == 0
