from django.db import models
from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=120, unique=True)
    body = models.TextField(default='body')
    slug = models.SlugField(max_length=250, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ['-updated']

    def get_absolute_url(self):
        return reverse("article:model_detail", kwargs={"id": self.id})
        