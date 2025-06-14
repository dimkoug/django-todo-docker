from django.urls import path


app_name = 'todo'

from .views import *

urlpatterns = [
    path('',TodoListView.as_view(),name='todo_list'),
    path('add/',TodoCreateView.as_view(),name='todo_add'),
    path('detail/<int:pk>/',TodoDetailView.as_view(),name='todo_view'),
    path('change/<int:pk>/',TodoUpdateView.as_view(),name='todo_change'),
    path('delete/<int:pk>/',TodoDeleteView.as_view(),name='todo_delete'),
]

