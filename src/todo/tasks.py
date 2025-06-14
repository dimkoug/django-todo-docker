from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

@shared_task
def send_todo_created_email(todo_id):
    from .models import Todo                    # local import avoids circularity
    todo = Todo.objects.select_related('profile__user').get(id=todo_id)

    send_mail(
        subject=f"New todo: {todo.name}",
        message=f"You just created a new todo:\n\n{todo.name}",
        from_email=None,                   # uses DEFAULT_FROM_EMAIL
        recipient_list=[todo.profile.user.email],
        fail_silently=False,
    )