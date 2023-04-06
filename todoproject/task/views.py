from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .form import CreateForm


@login_required
def index(request):
    user_id = request.user.id
    tasks = Task.objects.filter(user_id=user_id).order_by('-id')
    status = request.GET.get('status')
    q = request.GET.get('q')
    priority = request.GET.get('priority')
    if priority:
        tasks = tasks.filter(priority=priority)
    if status:
        tasks = tasks.filter(status=status)
    if q:
        tasks = tasks.filter(title__icontains=q)
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(user_id=user_id, title=title, deadline=datetime.now().date())
    ctx = {
        "object_list": tasks
    }
    return render(request, 'task/index.html', ctx)


@login_required
def edit(request, pk):
    task = get_object_or_404(Task, id=pk)
    user_id = request.user.id
    form = CreateForm(instance=task)
    if request.method == 'POST':
        form = CreateForm(data=request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task:index")
    ctx = {
        "form": form,
        'obj': task
    }
    return render(request, 'task/edit.html', ctx)


@login_required
def delete(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task:index')
    ctx = {
        'obj': task
    }
    return render(request, 'task/delete.html', ctx)