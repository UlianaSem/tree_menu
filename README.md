# Tree menu

## Описание проекта

Проект, реализующий древовидное меню

## Технологии

- Linux
- Python
- Poetry
- Django
- PostgreSQL
- Docker
- Docker Compose

## Зависимости

Зависимости, необходимые для работы проекта, указаны в файле pyproject.toml.

## Эндпоинты
1. `/menu/` - список меню
2. `/menu/<int:pk>/` - пункты меню

## Как запустить проект

Для запуска проекта необходимо выполнить следующие шаги:
1. При необходимости установите Docker и Docker Compose на компьютер с помощью инструкции https://docs.docker.com/engine/install/
2. Cклонируйте репозиторий себе на компьютер
3. Создайте файл .env и заполните его, используя образец из файла .env.example
4. Соберите образ с помощью команды `docker-compose build`
5. Запустите контейнеры с помощью команды `docker-compose up`

## Файл .env.example

1. `DATABASES_NAME, DATABASES_USER, DATABASES_PASSWORD, DATABASES_HOST` - данные для подключения к БД
2. `SECRET_KEY, DEBUG, ALLOWED_HOSTS`

## Доступ в админку

`username=admin`

`password=admin`

## Авторы

UlianaSem

## Связь с авторами

https://github.com/UlianaSem/
