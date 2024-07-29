from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Account
from .serializers import AccountSerializer
from .filters import AccountFilter
from pl_api.permissions import IsOwnerOrReadOnly


class AccountList(generics.ListAPIView):
  """
  List all accounts
  """
  queryset = Account.objects.annotate(
    leaf_count=Count('user__leaf', distinct=True),
  ).order_by('-created_at')
  serializer_class = AccountSerializer
  filter_backends = [
    filters.OrderingFilter,
    DjangoFilterBackend,
  ]
  filterset_class = AccountFilter
  ordering_fields = [
    'leaf_count',

  ]


class AccountDetail(generics.RetrieveUpdateAPIView):
  """
  Retrieve or update an account if you're the owner
  """
  permission_classes = [IsOwnerOrReadOnly]
  queryset = Account.objects.annotate(
    leaf_count=Count('user__leaf', distinct=True),
  ).order_by('-created_at')
  serializer_class = AccountSerializer