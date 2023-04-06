from django.urls import path
from .views import ProfileListCreateApiView, ProfileRUDApiView, MyAccountApiView
from rest_framework.authtoken import views

urlpatterns = [
    path('', ProfileListCreateApiView.as_view()),
    path('rud/<int:pk>/', ProfileRUDApiView.as_view()),
    path('login/', views.obtain_auth_token),
    path('my_account/', MyAccountApiView.as_view()),
]