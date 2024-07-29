from rest_framework import generics, permissions
from .models import Leaf
from .serializers import LeafSerializer
from pl_api.permissions import IsOwnerOrReadOnly


class LeafList(generics.ListCreateAPIView):
  """
  Lists leaves or creates a leaf if logged in
  """
  serializer_class = LeafSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  queryset = Leaf.objects.all()

  def perform_create(self, serializer):
      serializer.save(owner=self.request.user)


class LeafDetail(generics.RetrieveUpdateDestroyAPIView):
  """
  Retrieve a leaf and edit or delete it if you own it
  """
  serializer_class = LeafSerializer
  permission_classes = [IsOwnerOrReadOnly]
  queryset = Leaf.objects.all()