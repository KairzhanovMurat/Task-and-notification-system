from drf_spectacular.utils import OpenApiExample

example_task_list = [
    OpenApiExample(
        'Пример списка задач',
        value=[
            {
                'id': 1,
                'title': 'Рассылка',
                'description': 'Нужно сделать рассылку сообщений',
                'status': 'Pending',
                'due_date': '2013-01-29T12:34:56.000000Z'
            },
            {
                'id': 2,
                'title': 'Баг',
                'descrition': 'Исправить баг',
                'status': 'In Progress',
                'due_date': '2013-01-30T17:34:56.000000Z'
            }
        ],
        response_only=True,
    ),
]

example_task_detail = OpenApiExample(
    'Пример подробной информации о задаче',
    value={
        'id': 1,
        'title': 'Рассылка',
        'description': 'Нужно сделать рассылку сообщений',
        'status': 'Pending',
        'due_date': '2013-01-29T12:34:56.000000Z'
    },
    response_only=True,
)

example_task_create = OpenApiExample(
    'Пример создания/редактирования информации о задаче',
    value={
        'title': 'Баг',
        'description': 'Исправить баг',
        'status': 'in_progress',
        'due_date': '2013-01-29 12:34'
    },
    request_only=True,
)
