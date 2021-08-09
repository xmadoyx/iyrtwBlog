from django.db import models

# Create your models here.
class Article(models.Model):
    # giving data to our model
    # this model is for saving articles in database
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    # direct access from url to the url
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    # adding thumbnail for user
    # adding author name

    def __str__(self):
        return self.title
        # shows the title in articles list instead of django's default artice object(1)

    def snippet(self):
        return self.body[0:50] + '....'
        # only shows a snippet of article's body in articles list page
