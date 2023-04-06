from django.contrib import admin
from .models import Article, Category, Tag, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category']
    date_hierarchy = 'created_date'


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)