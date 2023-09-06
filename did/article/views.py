from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Article
def home(request):
    items = Article.objects.all()
    return render(
        request, 'article/index.html',
        {'items': items})

def detail(request, post):
    item = get_object_or_404(Article, slug=post)
    return render(request, 'article/detail.html', {'item': item})
