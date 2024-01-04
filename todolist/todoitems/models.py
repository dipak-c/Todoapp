from django.db import models


# Create your models here.
class Todolist(models.Model):
    todo = models.TextField()
