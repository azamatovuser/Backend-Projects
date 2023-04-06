from django.urls import path, include

app_name = 'course'

urlpatterns = [
    path('', include('apps.course.v1.urls'))
]