from gc import get_objects

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from scipy.stats import rdist

import tasks
from .forms import TaskForm
from .models import Task

# Create your views here.
@login_required
def task_list(request):
    if request.user.is_superuser:
        task = Task.objects.all()
    else:
        task = Task.objects.filter(assigned_to=request.user)

    return render(request, 'tasks/task_list.html', {'tasks', tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.assigned_to = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'tasks/task_list.html', {'form': form})

@login_required
def task_edit(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.user != task.assigned_to and not request.user.is_superuser:
        return redirect('task_list')

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')

    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_list.html', {'form': form})

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.user != task.assigned_to and not request.user.is_superuser:
        return redirect('task_list')
    if request.user == task.assigned_to or request.user.is_superuser:
        task.delete()

    return redirect('task_list')