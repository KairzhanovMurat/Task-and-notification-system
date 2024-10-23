from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from tasks import models, examples
from tasks.filters import TaskFilter
from tasks.permissions import IsOwnerOrReadOnly
from tasks.serializers import TaskSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Задачи текущего пользователя",
        description="Список всех задач текущего пользователя.",
        tags=['Задачи'],
        examples=examples.example_task_list

    ),
    retrieve=extend_schema(
        summary="Получение задачи",
        description="Получение информации о конкретной задаче.",
        tags=['Задачи'],
        examples=[examples.example_task_detail]
    ),
    create=extend_schema(
        summary="Создание новой задачи",
        description="Создание новой задачи для пользователя.",
        tags=['Задачи'],
        examples=[examples.example_task_create]
    ),
    update=extend_schema(
        summary="Обновление задачи",
        description="Обновление данных о задаче(доступно только владельцу).",
        tags=['Задачи'],
        examples=[examples.example_task_create]
    ),
    partial_update=extend_schema(
        summary="Частичное обновление задачи",
        description="Частичное обновление информации о задаче(доступно только владельцу).",
        tags=['Задачи'],
        examples=[examples.example_task_create]
    ),
    destroy=extend_schema(
        summary="Удаление задачи",
        description="Удаление задачи из базы данных(доступно только владельцу).",
        tags=['Задачи']
    )
)
@method_decorator(cache_page(60 * 10), name='list')
class TaskViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = TaskSerializer
    filterset_class = TaskFilter
    ordering_fields = '__all__'
    queryset = models.Task.objects.prefetch_related('user').all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
