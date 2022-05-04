from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# model pro seznam ukolu, vazba na uzivatele, nazev seznamu tasku
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
# model pro polozku seznamu tasku, nazev tasku a stav
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text