from django import forms

from core.forms import BootstrapForm

from .models import Todo

class TodoForm(BootstrapForm,forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('name',)


