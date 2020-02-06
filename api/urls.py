from django.conf.urls import url

from .views import create_task, get_result

urlpatterns = [
    url(r'create/task/', create_task, name='create_task'),
    url(r'get/result/', get_result, name='get_reult'),
]