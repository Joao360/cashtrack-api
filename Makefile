SHELL := /bin/sh

DJANGO_POSTFIX := 0.0.0.0:8000

run:
	python manage.py runserver $(DJANGO_POSTFIX)

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

superuser:
	python manage.py createsuperuser

shell:
	python manage.py shell