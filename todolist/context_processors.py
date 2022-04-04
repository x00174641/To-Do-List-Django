from .models import ToDoTask
from django.utils import timezone
from datetime import timedelta

def todotasks(request):
    if request.user.is_authenticated:
        tasks = ToDoTask.objects.filter(author=request.user,completed=False)
        taskscount = ToDoTask.objects.filter(author=request.user,completed=False).count
        for i in tasks:
            if timezone.now() + timedelta(minutes=60) >= i.due_date:
                i.completed = True
                i.save()    
        return dict(tasks=tasks,taskcount=taskscount)
    return {}