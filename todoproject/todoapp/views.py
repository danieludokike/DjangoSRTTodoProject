from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from .forms import TodoForm 


def task_list(request):
    """
    Handles displaying the list and the 'Create' form submission. 
    This is your primary single-page view.
    """
    todos = TodoItem.objects.all()
    
    if request.method == 'POST':
        form = TodoForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('task_list') 
    else:
        form = TodoForm()
        context = {
        'tasks': todos,        
        'create_form': form   
    }
    return render(request, 'task_list.html', context)


def task_update(request, pk):
    """
    Handles the 'Update' operation for an existing task.
    """
    task = get_object_or_404(TodoItem, pk=pk)
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TodoForm(instance=task)
    
    context = {
        'form': form,
        'task': task
    }
    return render(request, 'task_update_form.html', context)


def task_delete(request, pk):
    """
    Handles the 'Delete' confirmation (GET) and execution (POST).
    """
    task = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    
    context = {'task': task}
    return render(request, 'task_confirm_delete.html', context)