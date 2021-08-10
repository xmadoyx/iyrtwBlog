from django import forms
# forms are basically classes. we can use classes to create forms
from . import models

class CreateArticle(forms.ModelForm):
    # a form for creating articles by user
    class Meta:
        # with meta class we can assign attributes to our upper class
        model = models.Article
        # this model is like Article model from models.py
        fields = ['title', 'slug', 'body', 'image']
        # fields that we want for our createArticle class, which are the same as fields in Article model from models.py
        # date and time gets added automatically
