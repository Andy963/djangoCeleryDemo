import os
from django.conf import settings
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoCeleryDemo.settings')

# 实例化一个celery对象，其中的broker, backend在配置文件中
#app = Celery('djangoCeleryDemo',broker=settings.CELERY_BROKER_URL)
app = Celery('djangoCeleryDemo')
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace= 'CELERY')

# Load task modules from all registered Django app configs.
# 去每个注册app中读取tasks.py
app.autodiscover_tasks()
