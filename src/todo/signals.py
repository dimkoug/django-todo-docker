from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Todo
from .tasks import send_todo_created_email


@receiver(post_save, sender=Todo)
def todo_post_save(sender, instance, created, **kwargs):
    if created:
        send_todo_created_email.delay(instance.id)   # ← async