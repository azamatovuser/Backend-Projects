from django.urls import path
# from .views import blog, blog_single
from .views import BlogView, BlogDetailView

urlpatterns = [
    # path('', blog, name='blog'),
    # path('<int:pk>/', blog_single, name='blog-single'),
    path('', BlogView.as_view(), name='blog'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog-single'),
]