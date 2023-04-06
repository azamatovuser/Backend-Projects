from django.contrib import admin
from .models import Podcast, Category, Tag, Like, Season
from .models import Comment

admin.site.register(Podcast)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Season)