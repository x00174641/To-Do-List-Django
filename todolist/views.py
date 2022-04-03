from .models import ToDoTask
from django.views.generic.edit import CreateView

class TaskCreateView(CreateView):
    model = ToDoTask
    template_name = 'new_task.html'
    fields = ['title','due']