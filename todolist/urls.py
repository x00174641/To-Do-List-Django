from django.urls import path 
from .views import TaskCreateView, TaskUpdateView,TaskDeleteView,TasksCompleted,MarkTaskAsCompleted,ReverseACompletedTask

urlpatterns = [
    path('task/new/', TaskCreateView, name='task_new'),
    path('task/update/<id>', TaskUpdateView, name='task_update'),
    path('task/delete/<id>', TaskDeleteView, name='task_delete'),
    path('task/completed/', TasksCompleted, name='tasks_completed'),
    path('task/mark_as_completed/<id>', MarkTaskAsCompleted, name="task_mark_completed"),
    path('task/reverse_completed_task/<id>', ReverseACompletedTask, name="reverse_task_completed")
]