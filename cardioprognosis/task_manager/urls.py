from django.urls import path
from .views import task_list

app_name = 'task_manager'

urlpatterns = [
    path('tasks/', task_list, name='task_list'),
]