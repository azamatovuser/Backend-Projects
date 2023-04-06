from django.urls import path
from .views import bl

app_name = 'blogs'

urlpatterns = [
    path('blogs/', bl, name='list')
]