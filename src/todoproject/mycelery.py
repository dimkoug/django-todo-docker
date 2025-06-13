import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todoproject.settings")

app = Celery("todoproject")
app.config_from_object("django.conf:settings", namespace="CELERY")