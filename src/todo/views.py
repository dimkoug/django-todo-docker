from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

# Create your views here.
from .models import Todo
from .forms import TodoForm


class TodoListView(ListView):
    model = Todo



class TodoDetailView(DetailView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("todo:todo-list")


class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("todo:todo-list")


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo:todo-list")