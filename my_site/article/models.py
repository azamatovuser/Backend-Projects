from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Tag(models.Model):
    title = models.CharField(max_length=32)


class Category_more(models.Model):
    title = models.CharField(max_length=221)


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    content = models.TextField()
    image = models.ImageField(upload_to='static/image')
    slug = models.SlugField(unique=True)
    nima = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category_more, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)


#
# class Pc(models.Model):
#     keyboard = models.TextField()
#     mouse = models.TextField()
#     Monitor = models.TextField()
#     Case = models.TextField()
#
#
# class Book(models.Model):
#     Obloshka = models.ImageField()
#     title = models.CharField(max_length=221)
#     content = models.TextField(blank=True, null=True)
#     pages = models.IntegerField()
#     author = ForeignKey(User, on_delete=models.CASCADE)
