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
    queryset = Todo.objects.select_related('profile')
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(profile_id=self.request.user.profile)
        return queryset


class TodoDetailView(LoginRequiredMixin,DetailView):
    model = Todo
    queryset = Todo.objects.select_related('profile')
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(profile_id=self.request.user.profile)
        return queryset


class TodoCreateView(LoginRequiredMixin,SuccessUrlMixin,FormMixin,CreateView):
    model = Todo
    form_class = TodoForm

    def form_valid(self,form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)
        



class TodoUpdateView(LoginRequiredMixin,SuccessUrlMixin, FormMixin,UpdateView):
    model = Todo
    form_class = TodoForm
    queryset = Todo.objects.select_related('profile')
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(profile_id=self.request.user.profile)
        return queryset



class TodoDeleteView(LoginRequiredMixin,SuccessUrlMixin,DeleteView):
    model = Todo
    queryset = Todo.objects.select_related('profile')
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(profile_id=self.request.user.profile)
        return queryset
