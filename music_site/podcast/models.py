from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='cat_image/')


class Tag(models.Model):
    title = models.CharField(max_length=221)


class Season(models.Model):
    title = models.CharField(max_length=221)


class Podcast(models.Model):
    author = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    music = models.FileField(upload_to='music_files/')
    image = models.ImageField(upload_to='music_images/')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    views = models.IntegerField()
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    music = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name='music_like')


class Comment(models.Model):
    author = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE)
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name='comments')
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)