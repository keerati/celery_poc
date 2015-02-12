from __future__ import absolute_import

import os
import json

from celery import Celery
from celery.utils.log import get_task_logger

from django.conf import settings
from time import sleep

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_poc.settings')

app = Celery('celery_poc')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


logger = get_task_logger(__name__)

@app.task(bind=True)
def print_json(self, data):
    logger.info('start print_json')
    sleep(10)
    logger.info('got data %s' % data)

@app.task(bind=True)
def print_json_for_feed(self, data):
    logger.info('start print_json_for_feed')
    sleep(10)
    logger.info('got data %s' % data)
