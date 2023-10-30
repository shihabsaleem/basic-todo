from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .form import TodoForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.
class TaskList(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'todo'


class TaskDetail(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'


class TaskCreate(CreateView):
    model = Task
    template_name = 'add.html'
    context_object_name = 'todo'
    fields = 'name', 'priority', 'date'

    success_url = reverse_lazy('chome')


class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'delete.html'

    def get_success_url(self):
        return reverse_lazy('todoapp:chome')



class TaskUpdate(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('todoapp:chome')


def add(request):
    todo = Task.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')

        task = Task(name=name, priority=priority, date=date)
        task.save()

    return render(request, "home.html", {'todo': todo})


def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, "delete.html")


def details(request):
    task = Task.objects.all()
    return render(request, "details.html", {'task': task})


def update(request, taskid):
    task = Task.objects.get(id=taskid)
    frm = TodoForm(request.POST or None, instance=task)
    if frm.is_valid():
        frm.save()
        return redirect('/')

    return render(request, "update.html", {'frm': frm, 'task': task})
