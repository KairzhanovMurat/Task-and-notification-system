from django.db import models
from django.conf import settings


class Task(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        IN_PROGRESS = 'in_progress', 'In Progress'
        COMPLETED = 'completed', 'Completed'

    title = models.CharField(max_length=255, verbose_name="Название задачи")
    description = models.TextField(verbose_name="Описание задачи")
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name="Статус задачи"
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец задачи")
    due_date = models.DateTimeField(verbose_name="Дата и время завершения задачи")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "задачу"
        verbose_name_plural = "задачи"
