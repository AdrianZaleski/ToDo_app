from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

# Create your views here.


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'


class DetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task.html'


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
