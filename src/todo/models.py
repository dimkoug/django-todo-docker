from django.db import models


# Create your models here.
class Todo(models.Model):
    profile = models.ForeignKey("profiles.Profile", null=True,blank=True,on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    
    class Meta:
        default_related_name = 'todos'
        verbose_name = 'todo'
        verbose_name_plural = 'todos'
    
    def __str__(self):
        return f"{self.name}"




