from django.views.generic import CreateView, ListView, DetailView
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
