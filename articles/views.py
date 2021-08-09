from django.shortcuts import render
from . import models
# accessing our model from views.py and save its datas into a variable and pass it to render so we can access it from our html file

# Create your views here.
def articles_list(request):
    articles = models.Article.objects.all().order_by('date')
    # reaches for our Article model and its objects, ordered by one of its properties

    return render(request, 'articles/articleslist.html', {'articles': articles})
    # with the third argument, we're passing our 'articles' variable to render so we can access it from html file
