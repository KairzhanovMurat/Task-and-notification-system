


# Task and Notification System

Этот проект предоставляет API для управления задачами.

## Начало работы

### Предварительные требования

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Клонирование репозитория

```bash
git clone git@github.com:KairzhanovMurat/Task-and-notification-system.git

cd Task-and-notification-system
```

### Настройка

1. Переименуйте файл `.env.example` в `.env` и задайте ваши переменные окружения.

### Сборка и запуск приложения

```bash
docker-compose up --build -d
```
### Пополнение БД тестовыми данными

```bash
docker exec -it app sh -c "python manage.py loaddata users tasks notifications"
```


### Доступ к API

API будет доступно по адресу `http://localhost:8000`.

## Входные данные
- login: admin
- password: 1

### Запуск тестов

Для запуска тестов используйте следующую команду:

```bash
docker-compose exec -it app pytest
```


