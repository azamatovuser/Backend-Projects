from django.urls import path
from .models import Article
from .views import list, detail, edit, delete, create


app_name = 'articles'

urlpatterns = [
    path('', list, name='list'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('create/', create, name='create'),
]