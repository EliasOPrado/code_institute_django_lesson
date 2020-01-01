from django.apps import apps
from django.test import TestCase
from .apps import TodoConfig

class TestTodoConfig(TestCase):

    def test_app(self):
        self.assertEqual('todo', TodoConfig.item)
        self.assertEqual('Todo', apps.get_app_config('todo').name)
