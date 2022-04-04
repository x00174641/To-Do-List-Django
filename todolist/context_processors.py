from .models import ToDoTask
from django.utils import timezone
from datetime import timedelta
from django.core.paginator import Paginator , EmptyPage, InvalidPage

def todotasks(request):
    if request.user.is_authenticated:
        tasks = ToDoTask.objects.filter(author=request.user,completed=False)
        taskscount = ToDoTask.objects.filter(author=request.user,completed=False).count
        for i in tasks:
            if timezone.now() + timedelta(minutes=60) >= i.due_date:
                i.completed = True
                i.save()
        paginator = Paginator(tasks, 6)    
        try:
            page = int(request.GET.get("page", "1"))
        except:
            page = 1
        try:
            tasks = paginator.page(page)
        except (EmptyPage, InvalidPage):
            tasks = paginator.page(paginator.num_pages)
        return dict(tasks=tasks,taskcount=taskscount,page=page)
    return {}