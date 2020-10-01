from django.db import models

# Create your models here.


class Memory(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
