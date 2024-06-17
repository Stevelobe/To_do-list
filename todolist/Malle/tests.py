from django.test import TestCase
from .models import User, MalleTag, MalleTask

class MalleTaskModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(name="Test User", email="user@test.com", password="password123")
        self.tag1 = MalleTag.objects.create(name="Tag1")
        self.tag2 = MalleTag.objects.create(name="Tag2")

    def test_entry_creation(self):
        task = MalleTask.objects.create(
            title="Test Task",
            description="This is a test task.",
            due_date="2024-06-30",
            completed=False,
            user=self.user
        )
        self.assertEqual(MalleTask.objects.count(), 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.user, self.user)

    def test_entry_update(self):
        task = MalleTask.objects.create(
            title="Test Task",
            description="This is a test task.",
            due_date="2024-06-30",
            completed=False,
            user=self.user
        )
        task.title = "Updated Task"
        task.save()
        task.refresh_from_db()
        self.assertEqual(task.title, "Updated Task")

    def test_entry_deletion(self):
        task = MalleTask.objects.create(
            title="Test Task",
            description="This is a test task.",
            due_date="2024-06-30",
            completed=False,
            user=self.user
        )
        task_id = task.id
        task.delete()
        self.assertFalse(MalleTask.objects.filter(id=task_id).exists())

    def test_tag_assignment(self):
        task = MalleTask.objects.create(
            title="Test Task",
            description="This is a test task.",
            due_date="2024-06-30",
            completed=False,
            user=self.user
        )
        task.tags.add(self.tag1, self.tag2)
        self.assertEqual(task.tags.count(), 2)
        self.assertIn(self.tag1, task.tags.all())
        self.assertIn(self.tag2, task.tags.all())



