from django.db import models
from django.contrib.auth.forms import User


class Category(models.Model):
    title = models.CharField(max_length=221)


class Tag1(models.Model):
    title = models.CharField(max_length=221)


class Blog(models.Model):
    author = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag1)
    created_date = models.DateTimeField(auto_now_add=True)


class Comment_blog(models.Model):
    author = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE)
    podcast = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)