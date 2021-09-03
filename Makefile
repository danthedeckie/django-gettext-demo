virtual_env:
	python3 -m venv virtual_env
	./virtual_env/bin/pip install django

test: virtual_env
	./virtual_env/bin/python3 ./manage.py shell -c 'import test'
