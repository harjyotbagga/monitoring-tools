import os
from celery import Celery
from exporter import REDIS_BACKEND_URL, REDIS_BROKER_URL

config = {
    "task_default_queue": "application_queue",
}
app = Celery("monitoring_app", broker=REDIS_BROKER_URL,
             backend=REDIS_BACKEND_URL)
app.conf.update(**config)
