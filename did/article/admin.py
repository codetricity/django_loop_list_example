from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title', 'body']
    list_display = ['title', 'updated']

admin.site.register(Article, ArticleAdmin)
