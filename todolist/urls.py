from django.urls import path 
from .views import TaskCreateView

urlpatterns = [
    path('task/new/', TaskCreateView, name='task_new'),
]