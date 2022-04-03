from .models import ToDoTask

def todotasks(request):
    if request.user.is_authenticated:
        tasks = ToDoTask.objects.filter(author=request.user)
        return dict(tasks=tasks)
    return {}