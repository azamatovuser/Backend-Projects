from django.urls import path
from .views import index, list, detail, archive, like, ids_list

app_name = 'podcast'

urlpatterns = [
    path('', index, name='index'),
    path('list/', list, name='list'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('like/', like, name='like'),
    path('ids_list/', ids_list, name='ids_list'),
    path('archive/<int:pk>', archive, name='archive'),
]