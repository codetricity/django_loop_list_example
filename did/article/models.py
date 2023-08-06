from django.db import models
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=120, default='title')

    def __str__(self):
        return self.title
    