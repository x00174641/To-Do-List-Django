from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.

class ToDoTask(models.Model):
    task_name = models.CharField(max_length=30)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('due_date',)
        
    def __str__(self):
        return self.task_name 
        
    def get_absolute_url(self): 
        return reverse('home')