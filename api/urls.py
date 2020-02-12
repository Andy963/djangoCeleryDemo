from django.conf.urls import url

from .views import create_task, get_result, create_async_task, get_async_result

urlpatterns = [
    url(r'create/task/', create_task, name='create_task'),
    url(r'get/result/', get_result, name='get_result'),
    ## 定时任务
    url(r'create/async/task/', create_async_task, name='create_async_task'),
    url(r'get/async/result/', get_async_result, name='get_async_result'),
]

# 当在不同文件中存在同名task时，使用下面这种方式
# result1=app1.tasks.get("s1.add").delay(1,2)
# result2=app2.tasks.get("s1.mul").delay(3,2)
