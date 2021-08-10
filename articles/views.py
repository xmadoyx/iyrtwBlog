from django.shortcuts import render , HttpResponse , redirect
from . import models
# accessing our model from views.py and save its datas into a variable and pass it to render so we can access it from our html file
from django.contrib.auth.decorators import login_required
from . import forms
# this import is for being used in create_article function

# Create your views here.
def articles_list(request):
    articles = models.Article.objects.all().order_by('-date')
    # reaches for our Article model and its objects, ordered by one of its properties(=date)

    return render(request, 'articles/articleslist.html', {'articles': articles})
    # with the third argument, we're passing our 'articles' variable to render so we can access it from html file

def article_detail(request, slug):
    # capturing slug from urls.py with the second arguments that has the same name as its first path argument
    # return HttpResponse(slug)
    article = models.Article.objects.get(slug=slug)
    # get 'slug' objects from our 'Article' model that are equal to out article_detail slug function
    return render(request, 'articles/article_detail.html',{'article': article})
    # sending found slugs to out article_detail template

@login_required(login_url = "/accounts/login")
# this decorator requires the user to be logged in in order to create an article with create_article function, otherwise we should redirect the user to the login page
def create_article(request):
    if request.method == 'POST':
        # if the 'create' button was pushed
        form = forms.CreateArticle(request.POST, request.FILES)
        # request.FILES is for receiving image
        if form.is_valid:
            instance = form.save(commit = False)
            # receiving fomr's values, but not saving(=committing) form inside of database, instead putting them in instance variable, so we can get the author's name first before committing it to server
            instance.author = request.user
            instance.save()
            # save article with the author's name in server
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
        # if it's not a post-method, it's a get-method and it returns an empty form
    # getting the form for creating article and saving it on the server
    return render(request, 'articles/create_article.html', {'form': form})
    # we pass the form as the third argument so that it can be reached from template
