from django.urls import path


app_name = 'todo'

from .views import *

urlpatterns = [
    path('',TodoListView.as_view(),name='todo-list'),
    path('add/',TodoCreateView.as_view(),name='todo-add'),
    path('detail/<int:pk>/',TodoDetailView.as_view(),name='todo-view'),
    path('change/<int:pk>/',TodoUpdateView.as_view(),name='todo-change'),
    path('delete/<int:pk>/',TodoDeleteView.as_view(),name='todo-delete'),
]

