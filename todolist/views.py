from .models import ToDoTask
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = ToDoTask
    template_name = 'new_task.html'
    fields = ['task_name','due']

    def form_valid(self,form): #this sets the user as the current user when creating a new comment
        form.instance.author = self.request.user
        return super().form_valid(form)