from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Task
from .forms import TaskForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required

#@login_required(login_url="/admin/login/")
@login_required
@permission_required('todo_app.change_task', raise_exception=True)
def task_list(request):
    all_tasks = Task.objects.all()
    return render(request,'task_list.html',{'tasks':all_tasks})

@login_required
@permission_required('todo_app.add_task', raise_exception=True)
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

@login_required
@permission_required('todo_app.change_task', raise_exception=True)
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

@login_required
@permission_required('todo_app.delete_task', raise_exception=True)
def task_delete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('task_list')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(request)
        if user is not None:
            login(request, user)
            if request.GET.get('next') and request.GET.get('next')!='/logout/login/':
                return redirect(request.GET.get('next'))
            else:
                return redirect('/todo')
        else:
            error_message = 'Invalid username or password.'
            return render(request, 'login_page.html', {'error_message': error_message})
    else:
        return render(request, 'login_page.html')


def user_logout(request):
    logout(request)
    return redirect(reverse('user_login'))  # Replace 'home' with the desired URL after logout
