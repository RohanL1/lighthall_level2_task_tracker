from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.

def get_name(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        curr_user, flag_ = CustUser.objects.get_or_create(username = name)
        print(name , curr_user.id)
        return redirect(f'/task/{curr_user.id}/list/')
    return render(request, 'get_name.html')

def log_out(request):
    return redirect('/task/')


def list_tasks(request,pk):
    curr_user = get_object_or_404(CustUser, id = pk)
    task = Task.objects.filter(user = curr_user)
    
    context = {
        'user_id': curr_user.id,
        'tasks': task,
        'user_name' : curr_user.username,
    }
    return render(request, 'task_list.html', context=context)

def task_edit(request, pk) :
    task = get_object_or_404(Task, pk=pk)
    # print()

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(f'/task/{task.user.id}/list/')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    user_id = task.user.id
    task.delete()
    return redirect(f'/task/{user_id}/list/')

def task_create(request,u_pk):
    curr_user = get_object_or_404(CustUser, pk=u_pk)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = curr_user
            task.save()
            return redirect(f'/task/{u_pk}/list/')
    else:
        form = TaskForm()
    return render(request, 'task/task_form.html', {'form': form})
