from django.db import models
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Article(models.Model):
    title = models.CharField(max_length=120, unique=True)
    body = models.TextField(default='body')
    slug = models.SlugField(max_length=250, unique=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-updated']

    def get_absolute_url(self):
        return reverse("article:model_detail", kwargs={"id": self.id})
        