# Create your views here.
import datetime

from django.shortcuts import HttpResponse
from .tasks import add, mul
from celery.result import AsyncResult
from djangoCeleryDemo import celery_app


def create_task(request):
    print('请求来了')
    result = add.delay(2, 2)
    print('执行完毕')
    return HttpResponse(result.id)

def create_async_task(request):
    """创建定时任务"""
    # ETA一定要是utc时间

    ctime = datetime.datetime.now()
    utc_ctime = datetime.datetime.utcfromtimestamp(ctime.timestamp())

    s10 = datetime.timedelta(seconds=5)
    ctime_x = utc_ctime + s10
    print('async tasks')
    result = add.apply_async(args=(1,2),eta=ctime_x)
    return HttpResponse(result.id)

def get_result(request):
    nid = request.GET.get('nid')
    from celery.result import AsyncResult
    # from demos.celery import app
    from djangoCeleryDemo import celery_app
    # 取完数据仍在backends中，如果不需要执行result_object.forget()
    result_object = AsyncResult(id=nid, app=celery_app)
    # result_objcet.revoke() 取消任务，如果任务已经在执行，强制取消result_object.revoke(terminate=True)
    # get可能夯住，所以应该先判断status
    data = result_object.get()
    return HttpResponse(data)

def get_async_result(request):
    nid = request.GET.get('nid')
    result_object = AsyncResult(id=nid, app=celery_app)
    data = result_object.get()
    return  HttpResponse(data)