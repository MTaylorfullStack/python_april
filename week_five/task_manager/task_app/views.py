from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    return redirect('/tasks/new')


def new(request):
    return render(request, 'new.html')

def tasks(request):
    context = {
        'all_tasks': Task.objects.all()
    }
    return render(request, 'tasks.html', context)

def create_task(request):
    if request.method == 'POST':
        new_task = Task.objects.create(task=request.POST['task'])
        print(new_task)
        return redirect('/tasks')
    return redirect('/tasks/new')

def one_task(request, id):
    context = {
        'viewed_task':Task.objects.get(id=id)
    }
    return render(request, 'one_task.html', context)

def show_edit_page(request, id):
    context = {
        'edit_task': Task.objects.get(id=id)
    }
    return render(request, 'edit.html', context)

def process_edit(request, id):
    if request.method == 'POST':
        str_id = str(id)
        edit_task = Task.objects.get(id=id)
        edit_task.task = request.POST['task']
        edit_task.save()
        return redirect(f'/task/{str_id}')
    return redirect('/')

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/tasks')