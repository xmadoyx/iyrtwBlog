from django.urls import path
from . import views

app_name = "articles"
# unique name for the app so same names for paht, don't crash our program
urlpatterns = [
    path('', views.articles_list, name="list"),
    path('create', views.create_article, name="create"),
    # this path should be on top of sluf, because django compile these lines in order
    # if we don't write this path above slug, anything after 'articles/' will be put in slug and won't be dealt with the path that we want other than slug
    path('<slug>', views.article_detail, name="detail"),
    # capture the url
]
