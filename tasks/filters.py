import django_filters
from .models import Task


class TaskFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(field_name='status', lookup_expr='exact')
    due_date = django_filters.DateTimeFromToRangeFilter(field_name='due_date')

    class Meta:
        model = Task
        fields = ['status', 'due_date']
