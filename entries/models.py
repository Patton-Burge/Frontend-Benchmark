from django.db import models


class Entry(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    likes = models.IntegerField(default=0)
