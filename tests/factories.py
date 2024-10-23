import factory
from django.contrib.auth import get_user_model
from django.utils import timezone

from tasks.models import Task


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', 'defaultpassword')


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    title = 'test_title'
    description = factory.Faker('paragraph', nb_sentences=3)
    status = factory.Iterator(['pending', 'in_progress'])
    user = factory.SubFactory(UserFactory)
    due_date = factory.LazyFunction(timezone.now)
