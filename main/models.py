from django.db import models

# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length=200)

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()