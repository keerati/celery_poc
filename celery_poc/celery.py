from __future__ import absolute_import

import os
import json

from celery import Celery
from celery.utils.log import get_task_logger
from celery.signals import task_postrun

from django.conf import settings
from time import sleep
import requests

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


# ========== signals ===============
@task_postrun.connect(sender = print_json)
def post_to_websocket_server(**kwargs):
    logger.debug('post to websocket server!')
    headers   = {'content-type' : 'application/json' }
    post_dict = { "msg" : "req"}
    post_data = json.dumps(post_dict)
    response  = requests.post(
            "http://localhost:30000/post",
            data=post_data, headers=headers)
    logger.debug(response.text)
