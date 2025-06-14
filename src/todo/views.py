from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from core.mixins import *
from core.views import *
# Create your views here.
from .models import Todo
from .forms import TodoForm


class TodoListView(BaseListView):
    paginate_by = 10
    model = Todo
    queryset = Todo.objects.select_related('profile')
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(profile_id=self.request.user.profile)
        search = self.request.GET.get('search')
        if search and search.strip() != '':
            queryset = queryset.filter(name__icontains=search.strip())
        
        
        return queryset


class TodoDetailView(BaseDetailView):
    model = Todo
    queryset = Todo.objects.select_related('profile')
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(profile_id=self.request.user.profile)
        return queryset


class TodoCreateView(BaseCreateView):
    model = Todo
    form_class = TodoForm

    def form_valid(self,form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)
        



class TodoUpdateView(BaseUpdateView):
    model = Todo
    form_class = TodoForm
    queryset = Todo.objects.select_related('profile')
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(profile_id=self.request.user.profile)
        return queryset



class TodoDeleteView(BaseDeleteView):
    model = Todo
    queryset = Todo.objects.select_related('profile')
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(profile_id=self.request.user.profile)
        return queryset
