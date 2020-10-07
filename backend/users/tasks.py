from django.core import management

from memoirem.celery import app


@app.task
def clearsessions():
    management.call_command("clearsessions")
