from rest_framework import generics, permissions
from pl_api.permissions import IsOwnerOrReadOnly
from remember.models import Remember
from remember.serializers import RememberSerializer


class RememberList(generics.ListCreateAPIView):
    """
    List 'remembers' or add a 'remember' acknowledgment if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = RememberSerializer
    queryset = Remember.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RememberDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a 'remember' or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RememberSerializer
    queryset = Remember.objects.all()