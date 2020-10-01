from django.test import TestCase
from memories.models import Memory
import datetime
# Create your tests here.


class MemoryTestCase(TestCase):
    def setUp(self):
        title = "Title 1"
        content = "Content 1"
        created_at = datetime.datetime.now()
        Memory.objects.create(title, content, created_at)

        title = "Title 2"
        content = "Content 2"
        created_at = datetime.datetime.now()
        Memory.objects.create(title, content, created_at)

    def memory_sample_creation_test(self):
        title1 = Memory.objects.get(title="Title 1")
        title2 = Memory.objects.get(title="Title 2")
        self.assertEqual(title1.content, "Content 1")
        self.assertEqual(title2.content, "Content 2")
