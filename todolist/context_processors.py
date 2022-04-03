from .models import ToDoTask
from django.shortcuts import get_object_or_404

def todotasks(request):
    tasks = ToDoTask.objects.all()
    return dict(tasks=tasks)