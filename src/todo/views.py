from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from core.mixins import *

# Create your views here.
from .models import Todo
from .forms import TodoForm


class TodoListView(LoginRequiredMixin,ListView):
    model = Todo



class TodoDetailView(LoginRequiredMixin,DetailView):
    model = Todo


class TodoCreateView(LoginRequiredMixin,SuccessUrlMixin,FormMixin,CreateView):
    model = Todo
    form_class = TodoForm



class TodoUpdateView(LoginRequiredMixin,SuccessUrlMixin, FormMixin,UpdateView):
    model = Todo
    form_class = TodoForm



class TodoDeleteView(LoginRequiredMixin,SuccessUrlMixin,DeleteView):
    model = Todo
