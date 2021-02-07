Тестовое задание на python django celery

Порядок действий:
1. docker-compose up --build
2. docker-compose run --rm django-app python manage.py createsuperuser
3. docker-compose run --rm django-app python manage.py test
4. http://127.0.0.1:8000/admin/pages/page/
5. http://127.0.0.1:8000/api/pages/
6. http://127.0.0.1:8000/api/pages/1/
