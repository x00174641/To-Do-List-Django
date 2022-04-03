from django.db import models
from django.urls import reverse
# Create your models here.

class ToDoTask(models.Model):
    title = models.CharField(max_length=200)
    due = models.DateTimeField()
    
    class Meta:
        ordering = ('due',)

    def __str__(self):
        return self.title 
        
    def get_absolute_url(self): 
        return reverse('home')