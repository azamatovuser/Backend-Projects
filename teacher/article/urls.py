from django.urls import path
from .views import index, detail, delete, edit, create

app_name = 'articles'

urlpatterns = [
    path('article/', index, name='list'),
    path('article/detail/<slug:slug>/', detail, name='detail'),
    path('article/create/', create, name='create'),
    path('article/edit/<slug:slug>/', edit, name='edit'),
    path('article/delete/<slug:slug>/', delete, name='delete')
]