from rest_framework import serializers

from tasks.models import Task
from .tasks import send_task_completion_notification


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ['user']
        read_only_fields = ['id', ]

    def update(self, instance, validated_data):
        new_status = validated_data.get('status', instance.status)
        if new_status != instance.status and new_status == 'completed':
            send_task_completion_notification.delay(instance.id)
        return super().update(instance, validated_data)
