from django import forms
from .models import Article, Tag, Category_more


class EditForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image', 'category', 'tags']


class Createform(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['author', 'title', 'content', 'image', 'category', 'tags', 'slug', 'created_date']
        exclude = ['author', 'slug', 'created_date']