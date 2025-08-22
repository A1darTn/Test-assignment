# Music Catalog API

Каталог музыки с использованием Django REST Framework, предоставляющий API для управления исполнителями, альбомами и песнями.

## Функциональность

- Управление исполнителями (артистами)
- Управление альбомами с указанием года выпуска
- Управление песнями с возможностью добавления в разные альбомы под разными номерами треков
- Автоматическая документация API через Swagger UI
- Поддержка Docker для простого развертывания

## Технологии

- Python 3.9
- Django 3.2
- Django REST Framework 3.13
- SQLite (для разработки)
- Docker & Docker Compose
- drf-yasg (Swagger документация)

## Быстрый старт

### Запуск с Docker Compose

1. **Клонируйте репозиторий:**
```bash
git clone https://github.com/A1darTn/Test-assignment
```
2. **Запустите контейнеры:**
```bash
docker-compose up --build
```
3. **Примените миграции базы данных (в новом терминале):**
```bash
docker-compose exec web python manage.py migrate
```
4. **Создайте суперпользователя (опционально):**
```bash
docker-compose exec web python manage.py createsuperuser
```
5. **Откройте в браузере:**
- API: http://localhost:8000/api/
- Swagger документация: http://localhost:8000/swagger/
- Админка Django: http://localhost:8000/admin/

## Примеры запросов

### Создание исполнителя

```bash
curl -X POST "http://localhost:8000/api/artists/" \
  -H "Content-Type: application/json" \
  -d '{"name": "The Beatles"}'
```
### Создание альбома

```bash
curl -X POST "http://localhost:8000/api/albums/" \
  -H "Content-Type: application/json" \
  -d '{"title": "Abbey Road", "artist": 1, "release_year": 1969}'
```
### Создание песни и добавление в альбом

```bash
# Сначала создаем песню
curl -X POST "http://localhost:8000/api/songs/" \
  -H "Content-Type: application/json" \
  -d '{"title": "Come Together"}'

# Затем добавляем ее в альбом с номером трека
# (этот endpoint нужно будет реализовать дополнительно)
```
