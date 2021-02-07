Тестовое задание на python django celery

Порядок действий:
1. docker-compose up --build
2. docker-compose run --rm django-app python manage.py createsuperuser
   docker-compose run --rm django-app python manage.py test
3. http://127.0.0.1:8000/admin/pages/page/
4. http://127.0.0.1:8000/api/pages/
5. http://127.0.0.1:8000/api/pages/1/
