from django.urls import path
from .views import course, CourseDetailView, lesson_detail


urlpatterns = [
    path('', course, name='course'),
    path('detail/<int:pk>/', CourseDetailView.as_view(), name='course-single'),
    path('detail/<int:course_id>/lesson/<int:pk>/', lesson_detail, name='lesson_detail'),
]