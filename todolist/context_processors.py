from .models import ToDoTask

def todotasks(request):
    if request.user.is_authenticated:
        tasks = ToDoTask.objects.filter(author=request.user)
        taskscount = ToDoTask.objects.filter(author=request.user).count
        return dict(tasks=tasks,taskcount=taskscount)
    return {}