from django.contrib import admin
from .models import Article, Comment, Tag, Category, SubContent, SubContentImage

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(SubContent)
admin.site.register(SubContentImage)