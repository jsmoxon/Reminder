web: python reminder/manage.py run_gunicorn -b "0.0.0.0:$PORT" -w 3 --log-level info --settings=settings.prod
scheduler: python reminder/manage.py celeryd -B -E --settings=settings.prod

