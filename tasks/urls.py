from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tasks import views

router = DefaultRouter()
router.register('tasks', views.TaskViewSet, basename='tasks')

app_name = 'tasks'

urlpatterns = [
    path('', include(router.urls))
]
