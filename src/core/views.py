from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Todo


def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'index.html', {"todo_items": todo_items})


@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    created_obj = Todo.objects.create(added_date=current_date, text=content)
    return redirect(home)


@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect(home)


@csrf_exempt
def update_todo(request, todo_id):
    new = request.GET['new']
    update_obj = Todo.objects.filter(id=todo_id).update(text=new)
    return redirect(home)

