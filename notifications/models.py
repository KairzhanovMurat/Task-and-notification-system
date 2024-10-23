from django.db import models


class Notification(models.Model):
    task = models.ForeignKey("tasks.Task", on_delete=models.CASCADE, verbose_name="Задача",
                             related_name="notifications")
    message = models.TextField(verbose_name="Текст уведомления")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания уведомления")

    def __str__(self):
        return f"Уведомление для задачи: {self.task.title}"

    class Meta:
        verbose_name = "уведомление"
        verbose_name_plural = "уведомления"
