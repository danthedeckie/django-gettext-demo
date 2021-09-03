virtual_env:
	python3 -m venv virtual_env
	./virtual_env/bin/pip install django

test: virtual_env
	./virtual_env/bin/python3 ./manage.py shell -c 'import test'

update_messages: virtual_env
	./virtual_env/bin/python3 ./manage.py makemessages -i virtual_env -l es
	./virtual_env/bin/python3 ./manage.py compilemessages -i virtual_env -l es

