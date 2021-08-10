from django.db import models
from django.contrib.auth.models import User
# importing our user model

# Create your models here.
class Article(models.Model):
    # giving data to our model
    # this model is for saving articles in database
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    # direct access from url to the url
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(default='default.jpg',blank=True)
    # adding thumbnail for articles, which is optional and uses default picture in case of (super)user not uploading one
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    # adding user's name as author name by connecting our article model to our user model with a foregin key

    def __str__(self):
        return self.title
        # shows the title in articles list instead of django's default artice object(1)

    def snippet(self):
        return self.body[0:50] + '....'
        # only shows a snippet of article's body in articles list page
