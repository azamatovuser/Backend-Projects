from rest_framework import generics, permissions
from .serializers import ContactSerializer
from ..models import Contact


class ContactListCreateApiView(generics.ListCreateAPIView):
    queryset = Contact.objects.all
    serializer_class = ContactSerializer


class ContactRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]