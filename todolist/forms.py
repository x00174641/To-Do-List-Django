from django.forms import ModelForm
from django import forms 
from .models import ToDoTask

# Create your views here.

class InputTypeDate(forms.DateInput):
    input_type = 'date'
    
class InputTypeTime(forms.TimeInput):
    input_type = 'time'

class ToDoTaskForm(ModelForm):
    class Meta:
        model = ToDoTask
        fields = ('task_name','due_date','due_time')
        widgets = {'due_date': InputTypeDate(),'due_time': InputTypeTime}