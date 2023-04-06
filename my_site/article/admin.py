from django.contrib import admin
from .models import Article, Tag, Category_more


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'image', 'slug', 'created_date', 'nima']
#
#
# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     list_display = ['title']
#
#
# @admin.register(Category_more)
# class Category_moreAdmin(admin.ModelAdmin):
#     list_display = ['title']
