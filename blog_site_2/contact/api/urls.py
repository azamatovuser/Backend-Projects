from django.urls import path
from .views import ContactListCreateApiView, ContactRUDApiView

urlpatterns = [
    path('', ContactListCreateApiView.as_view()),
    path('rud/<int:pk>/', ContactRUDApiView.as_view()),
]