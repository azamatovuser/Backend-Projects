from django.urls import path
from .views import recipe_list, recipe_detail, recipe_create, recipe_update, recipe_delete, tag_create, tag_detail
from .views import tag_delete, tag_update, tag_list, ing_create, ing_update, ing_delete, my_recipes

app_name = 'recipes'

urlpatterns = [
    path('list/', recipe_list, name='list'),
    path('my/list/', my_recipes, name='my_list'),
    path('detail/<slug:slug>/', recipe_detail, name='detail'),
    path('create/', recipe_create, name='create'),
    path('update/<slug:slug>/', recipe_update, name='update'),
    path('delete/<slug:slug>/', recipe_delete, name='delete'),

    path('tag/list/', tag_list, name='tag_list'),
    path('tag/detail/<int:pk>/', tag_detail, name='tag_detail'),
    path('tag/create/', tag_create, name='tag_create'),
    path('tag/update/<int:pk>/', tag_update, name='tag_update'),
    path('tag/delete/<int:pk>/', tag_delete, name='tag_delete'),

    path('<slug:recipe_slug>/ing/create/', ing_create, name='ing_create'),
    path('<slug:recipe_slug>/ing/update/<int:pk>/', ing_update, name='ing_update'),
    path('<slug:recipe_slug>/ing/delete/<int:pk>/', ing_delete, name='ing_delete'),
]