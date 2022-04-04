from audioop import reverse
from django.shortcuts import render,redirect,get_object_or_404
from .forms import ToDoTaskForm
from django.contrib.auth.decorators import login_required
from .models import ToDoTask
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta, datetime

@login_required
def TaskCreateView(request):
    if request.method == 'POST':
        form = ToDoTaskForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            print(form.instance.due_date)
            messages.success(request, "{} has been added to your to-do list!".format(form.instance.task_name))
            return redirect('home')
    else:
        form = ToDoTaskForm()
    return render(request, 'new_task.html', {'form': form})

@login_required
def TaskUpdateView(request,id):
    obj = get_object_or_404(ToDoTask, id=id)
    form = ToDoTaskForm(request.POST or None, instance = obj)
    if obj.author != request.user:
        messages.error(request, "You cannot update this task as you dont own the rights to it!")
        return redirect('home')
    else:
        if form.is_valid():
            form.save()
            messages.success(request, "{} has been updated!".format(form.instance.task_name))
            return redirect('home')
    return render(request,'update_task.html', {'form':form})

@login_required
def TaskDeleteView(request,id):
    obj = get_object_or_404(ToDoTask, id = id)
    if obj.author != request.user:
        messages.error(request, "You cannot delete this task as you dont own the rights to it!")
        return redirect('home')
    else:
        messages.success(request, "{} has been deleted!".format(obj.task_name))
        obj.delete()
    return redirect('home')

@login_required
def MarkTaskAsCompleted(request,id):
    obj = get_object_or_404(ToDoTask, id = id)
    if obj.completed == True:
        messages.error(request, "You already have this task marked as complete!")
        return redirect('home')
    if obj.author != request.user:
        messages.error(request, "You cannot mark this task as complete as you dont own the rights to it!")
        return redirect('home')
    else:
        messages.success(request, "{} has been marked as complete! Good job!".format(obj.task_name))
        obj.completed = True
        obj.save()
    return redirect('home')

@login_required
def TasksCompleted(request):
    tasks_completed = ToDoTask.objects.filter(author=request.user,completed=True)
    tasks_completed_count = ToDoTask.objects.filter(author=request.user,completed=True)

    return render(request,'completed_tasks.html', {'tasks_completed': tasks_completed,'task_comp_count': tasks_completed_count})

@login_required
def ReverseACompletedTask(request,id):
    obj = get_object_or_404(ToDoTask, id = id)
    if obj.completed == False:
        messages.error(request, "This task is currently active!")
        return redirect('home')
    if obj.author != request.user:
        messages.error(request, "You cannot reverse this task as uncomplete as you dont own the rights to it!")
        return redirect('home')
    else:
        obj.completed = False
        new_time_if_expired = timezone.now() + timedelta(minutes=60) + timedelta(days=7)
        if timezone.now() + timedelta(minutes=60) >= obj.due_date:
            messages.success(request, "{} has been reversed! However the time you set before has been due. I have set your new due date to {}!".format(obj.task_name, new_time_if_expired))
            obj.due_date = new_time_if_expired
        else:
            messages.success(request, "{} has been reversed with your old due time!".format(obj.task_name))
        obj.save()
    return redirect('home')

# class TaskCreateView(LoginRequiredMixin, CreateView):
#     model = ToDoTask
#     template_name = 'new_task.html'
#     fields =  ['task_name','due_date','due_time']

#     def form_valid(self,form): #this sets the user as the current user when creating a new comment
#         form.instance.author = self.request.user
#         return super().form_valid(form)