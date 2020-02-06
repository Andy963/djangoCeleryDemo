# Create your views here.
from django.shortcuts import HttpResponse
from .tasks import add

def create_task(request):
    print('请求来了')
    result = add.delay(2, 2)
    print('执行完毕')
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
