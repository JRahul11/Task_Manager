from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import TaskModel
from .forms import NewTaskForm
import datetime


def home(request):
    user = request.user
    empty = False
    if request.user.is_authenticated:
        task = TaskModel.objects.filter(user=user, iscompleted=False)
        if not task.exists():
            empty = True
        context = {
            'task': task,
            'empty': empty,
        }
        return render(request, "task_app/home.html", context)
    else:
        return redirect("user_login")


def sortnew(request):
    user = request.user
    empty = False
    task = TaskModel.objects.filter(
        user=user, iscompleted=False).order_by('-date')
    context = {
        'task': task,
        'empty': empty,
    }
    return render(request, "task_app/home.html", context)


def sortpriority(request):
    user = request.user
    empty = False
    task = TaskModel.objects.filter(
        user=user, iscompleted=False).order_by('-priority', 'date')
    context = {
        'task': task,
        'empty': empty,
    }
    return render(request, "task_app/home.html", context)


def history(request):
    user = request.user
    empty = False
    task = TaskModel.objects.filter(user=user, iscompleted=True)
    if not task.exists():
        empty = True
    context = {
        'task': task,
        'empty': empty,
    }
    return render(request, "task_app/history.html", context)


def newtask(request):
    user = request.user
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            priority = form.cleaned_data.get('priority')
            task = TaskModel.objects.create(
                user=user, title=title, description=description, priority=priority, date=timezone.now())
            return redirect('home')
    else:
        form = NewTaskForm()

    context = {
        'form': form,
    }
    return render(request, "task_app/newtask.html", context)


def updatetask(request, task_id):
    user = request.user
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            priority = form.cleaned_data.get('priority')
            TaskModel.objects.filter(user=user, id=task_id).update(
                title=title, description=description, priority=priority, date=timezone.now())
        return redirect('home')
    else:
        form = NewTaskForm()

    context = {
        'form': form,
    }
    return render(request, "task_app/updatetask.html", context)


def deletetask(request, task_id):
    user = request.user
    task = get_object_or_404(TaskModel, user=user, id=task_id)
    task.delete()
    if task.iscompleted == False:
        return redirect('home')
    else:
        return redirect('history')


def complete(request, task_id):
    user = request.user
    TaskModel.objects.filter(user=user, id=task_id).update(
        iscompleted=True, date=timezone.now())
    return redirect('home')
