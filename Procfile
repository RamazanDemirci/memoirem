web: gunicorn memoirem.wsgi --chdir backend --limit-request-line 8188 --log-file -
worker: celery worker --workdir backend --app=memoirem -B --loglevel=info
