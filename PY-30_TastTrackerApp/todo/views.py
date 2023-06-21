from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .forms import Todo, TodoForm

# ------------------------------------------------------------
# Function Based Views
# ------------------------------------------------------------

# List:
def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'list.html', context)

# Add:
def todo_add(request):
    # create a form instance and populate it with data from the request:
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        # Add a message to the request using the 'success' level
        messages.success(request, 'Task added successfully!')
        # Redirect to the list view
        return redirect('todo_list') # name of the url pattern or url path('/list')
    context = {
        'form': form,
    }
    return render(request, 'add.html', context)

# Update:
def todo_update(request, pk):
    # get the object:
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)
    if request.method== "POST":
        # update the object with new data:
        form = TodoForm(data=request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated.')
            return redirect("todo_list")
    return render(request, 'update.html', {
        'form': form,
        'todo': todo
    })

# Delete:
def todo_delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    messages.success(request, 'Task deleted.')
    return redirect("todo_list")