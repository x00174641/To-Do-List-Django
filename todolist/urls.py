from django.urls import path 
from .views import TaskCreateView

urlpatterns = [
    path('task/new/', TaskCreateView.as_view(), name='post_new'),
]