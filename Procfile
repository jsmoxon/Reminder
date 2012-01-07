web: bin/gunicorn_django -b 0.0.0.0:$PORT reminder/settings.py
worker: python reminder/manage.py celeryd -E -B --loglevel=INFO
worker: python reminder/manage.py celerybeat --loglevel=INFO