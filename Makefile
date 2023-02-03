run:
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate

admin:
	python manage.py createsuperuser

shell:
	python manage.py shell

test:
	python manage.py test

collect:
	python manage.py collectstatic
