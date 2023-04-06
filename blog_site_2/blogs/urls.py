from django.urls import path, include
from .views import index, detail, list

app_name = 'blogs'

urlpatterns = [
    path('', index, name='index'),
    path('list/', list, name='list'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('api/', include('blogs.api.urls'))
]