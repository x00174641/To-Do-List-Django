from django.contrib import admin

# Register your models here.
from .models import ToDoTask

admin.site.register(ToDoTask)