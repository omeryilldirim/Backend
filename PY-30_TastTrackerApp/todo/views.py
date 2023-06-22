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
    # return render(request, 'add.html', context)
    return render(request, 'add_update.html', context)

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
    context = {
        'form': form,
        'todo': todo
    }
    # return render(request, 'update.html', context)
    return render(request, 'add_update.html', context)

# Delete:
def todo_delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    messages.success(request, 'Task deleted.')
    # no need template
    return redirect("todo_list")


# ------------------------------------------------------------
# Function Based Views
# ------------------------------------------------------------
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    DetailView,
)
from django.urls import reverse_lazy

class TodoListView(ListView):
    model = Todo
    ordering = ['-id']
    # template_name = 'todo_list.html'   # template arayacağı path -> after 'templates/' default: 'modelname/modelname_list.html'


class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo_list')
    # template_name = 'todo_form.html'   # template arayacağı path -> after 'templates/' default: 'modelname/modelname_form.html'

    def post(self, request, *args, **kwargs):
        messages.success(request, 'New task added successfully!')
        return super().post(request, *args, **kwargs)


class TodoDetailView(DetailView):
    model = Todo
    # template_name = 'todo_detail.html'   # template arayacağı path -> after 'templates/' default: 'modelname/modelname_detail.html'


class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo_list')
    # template_name = 'todo_form.html'   # template arayacağı path -> after 'templates/' default: 'modelname/modelname_form.html'

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Task updated successfully!')
        return super().post(request, *args, **kwargs)


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')
    # template_name = 'todo_confirm_delete.html'   # template arayacağı path -> after 'templates/' default: 'modelname/modelname_form.html'