format:  ## Lint and static-check
	clear
	black .
	flake8 .

start:
	python manage.py runserver