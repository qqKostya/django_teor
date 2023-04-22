format:  ## Lint and static-check
	clear
	black django_example/
	flake8 django_example/

start:
	python django_example/manage.py runserver