from django.forms import ModelForm
from django import forms 
from .models import ToDoTask

# Create your views here.

class InputTypeDate(forms.DateTimeInput):
    input_type = 'datetime-local'
    
class ToDoTaskForm(ModelForm):
    class Meta:
        model = ToDoTask
        fields = ('task_name','due_date')
        widgets = {'due_date': InputTypeDate()}