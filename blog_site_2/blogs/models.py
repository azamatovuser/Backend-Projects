from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=221)


class Tag(models.Model):
    title = models.CharField(max_length=221)


class Article(models.Model):
    author = models.ForeignKey("profiles.Profile", on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    description = models.TextField()
    image = models.ImageField(upload_to='articles/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='article')
    tags = models.ManyToManyField(Tag)
    created_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    author = models.ForeignKey("profiles.Profile", on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


class SubContent(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE, related_name='subcontent')
    description2 = models.TextField()


class SubContentImage(models.Model):
    sub_content = models.ForeignKey(SubContent, on_delete=models.CASCADE, related_name='subcontentimage')
    image2 = models.ImageField()
    is_wide = models.BooleanField()