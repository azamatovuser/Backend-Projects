from rest_framework import generics, permissions, views
from rest_framework.response import Response
from .serializers import ProfileSerializer
from ..models import Profile


class ProfileListCreateApiView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MyAccountApiView(views.APIView):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"detail":"login is needed"})
        profile = Profile.objects.filter(user_id=request.user.id).first() or None
        if profile:
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        return Response({"detail":"not found"})


