from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from unittest import mock

from .models import Todo


class TodoModelTestCase(TestCase):
    def test_str_representation(self):
        todo = Todo(name="Sample")
        self.assertEqual(str(todo), "Sample")


class TodoListViewTestCase(TestCase):
    def setUp(self):
        user_cls = get_user_model()
        self.user = user_cls.objects.create_user(email="user@example.com", password="pass")
        self.other = user_cls.objects.create_user(email="other@example.com", password="pass")
        Todo.objects.create(name="Todo 1", profile=self.user.profile)
        Todo.objects.create(name="Other Todo", profile=self.other.profile)
        self.client = Client()

    def test_login_required(self):
        url = reverse("todo:todo_list")
        response = self.client.get(url)
        login_url = reverse("login")
        self.assertRedirects(response, f"{login_url}?next={url}")

    def test_list_shows_only_user_todos(self):
        self.client.login(email="user@example.com", password="pass")
        response = self.client.get(reverse("todo:todo_list"))
        todos = list(response.context["object_list"].values_list("name", flat=True))
        self.assertEqual(todos, ["Todo 1"])


class SendTodoCreatedEmailTestCase(TestCase):
    def setUp(self):
        user_cls = get_user_model()
        self.user = user_cls.objects.create_user(email="test@example.com", password="pass")
        self.todo = Todo.objects.create(name="Task", profile=self.user.profile)

    @mock.patch("todo.tasks.send_mail")
    def test_email_sent(self, mocked_send_mail):
        from .tasks import send_todo_created_email

        send_todo_created_email(self.todo.id)

        mocked_send_mail.assert_called_with(
            subject=f"New todo: {self.todo.name}",
            message=f"You just created a new todo:\n\n{self.todo.name}",
            from_email=None,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

