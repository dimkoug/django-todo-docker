from django import forms

from core.forms import BootstrapForm

from .models import Todo

class TodoForm(BootstrapForm,forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)


