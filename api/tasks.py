from celery import shared_task
from djangoCeleryDemo.celery import app


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)