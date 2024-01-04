from django.contrib import admin
from .models import Todolist


# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ("todo",)


admin.site.register(Todolist, TodoAdmin)
