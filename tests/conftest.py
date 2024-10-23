import pytest
from celery import Celery
from rest_framework.test import APIClient

from tests.factories import TaskFactory, UserFactory


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def authenticated_client(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def task(user):
    return TaskFactory(user=user)


@pytest.fixture(scope="session")
def celery_config():
    return {
        'broker_url': 'memory://',
        'result_backend': 'rpc://',
        'task_always_eager': True,
        'task_eager_propagates': True,
    }


@pytest.fixture(scope="session")
def celery_app(celery_config):
    app = Celery('test_app')
    app.conf.update(celery_config)
    return app
