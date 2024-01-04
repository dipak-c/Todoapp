from django.shortcuts import render, redirect
from todoitems.models import Todolist


def home(request):
    if request.method == "POST":
        todo = request.POST.get("todolist")
        list = Todolist(todo=todo)
        list.save()

    todoData = Todolist.objects.all()

    data = {
        "data": todoData,
    }
    return render(request, "index.html", data)


def delete(request, todo_id):
    item_to_delete = Todolist.objects.get(id=todo_id)
    item_to_delete.delete()
    return redirect("todolist")
