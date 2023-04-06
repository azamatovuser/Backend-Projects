from django.urls import path, include

app_name = 'blog'

urlpatterns = [
    path('', include('apps.blog.v1.urls'))
]