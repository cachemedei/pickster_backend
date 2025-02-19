release: python pickster/manage.py migrate
web: gunicorn --pythonpath pickster pickster.wsgi --log-file -