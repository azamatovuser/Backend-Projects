from django.urls import path
from .views import index

app_name = 'about'

urlpatterns = [
    path('about/', index, name='index')
]