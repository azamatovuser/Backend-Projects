from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=221)
    phone = models.CharField(max_length=221)
    email = models.EmailField()
    message = models.TextField()