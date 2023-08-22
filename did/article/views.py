from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Article
def home(request):
    items = Article.objects.all()
    return render(
        request, 'article/index.html',
        {'items': items})

def detail(request, id):
    item = get_object_or_404(Article, id=id)

    response = f"<p>title is: {item.title}</p>"
    response += f"<p>id is: {item.id} </p>"

    return HttpResponse(response)
