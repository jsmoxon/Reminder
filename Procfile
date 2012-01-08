web: python reminder/manage.py run_gunicorn -b "0.0.0.0:$PORT"
worker: python reminder/manage.py celeryd -E -B --loglevel=INFO


