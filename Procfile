web: bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT reminder/settings.py
worker: python reminder/manage.py celeryd -E -B --loglevel=INFO
