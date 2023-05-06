from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    all_tasks = Task.objects.all()
    return render(request,'task_list.html',{'tasks':all_tasks})

def task_create(request):
    print(request)
    if request.method == "POST":
        print(f'data{request.POST}')
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    form = TaskForm()
    return render(request,'task_create.html',{'form':form})

def task_update(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        print(f'data{request.POST}')
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    
    return render(request,'task_update.html',{'form':form})


def task_delete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('task_list')
