from django.shortcuts import render,redirect
from .forms import ToDoTaskForm
from django.contrib.auth.decorators import login_required

@login_required
def TaskCreateView(request):
    if request.method == 'POST':
        form = ToDoTaskForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('home')
    else:
        form = ToDoTaskForm()
    return render(request, 'new_task.html', {'form': form})
    
# class TaskCreateView(LoginRequiredMixin, CreateView):
#     model = ToDoTask
#     template_name = 'new_task.html'
#     fields =  ['task_name','due_date','due_time']

#     def form_valid(self,form): #this sets the user as the current user when creating a new comment
#         form.instance.author = self.request.user
#         return super().form_valid(form)