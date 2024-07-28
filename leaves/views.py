from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Leaf
from .serializers import LeafSerializer
from pl_api.permissions import IsOwnerOrReadOnly


class LeafList(APIView):
  serializer_class = LeafSerializer
  permission_classes = [
    permissions.IsAuthenticatedOrReadOnly
  ]

  def get(self, request):
    leaves = Leaf.objects.all()
    serializer = LeafSerializer(
      leaves, many=True, context={'request': request}
    )
    return Response(serializer.data)

  def post(self, request):
    serializer = LeafSerializer(
      data=request.data, context={'request': request}
    )
    if serializer.is_valid():
      serializer.save(owner=request.user)
      return Response(
        serializer.data, status=status.HTTP_201_CREATED
      )
    return Response(
      serializer.errors, status=status.HTTP_400_BAD_REQUEST
    )

class LeafDetail(APIView):
  permission_classes = [IsOwnerOrReadOnly]
  serializer_class = LeafSerializer

  def get_object(self, pk):
    try:
      leaf = Leaf.objects.get(pk=pk)
      self.check_object_permissions(self.request, leaf)
      return leaf
    except Leaf.DoesNotExist:
      raise Http404

  def get(self, request, pk):
    leaf = self.get_object(pk)
    serializer = LeafSerializer(
      leaf, context={'request': request}
    )
    return Response(serializer.data)

  def put(self, request, pk):
    leaf = self.get_object(pk)
    serializer = LeafSerializer(
      leaf, data=request.data, context={'request': request}
    )
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(
      serializer.errors, status=status.HTTP_400_BAD_REQUEST
    )

  def delete(self, request, pk):
    leaf = self.get_object(pk)
    leaf.delete()
    return Response(
      status=status.HTTP_204_NO_CONTENT
    )