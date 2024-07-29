from rest_framework import generics
from .models import Account
from .serializers import AccountSerializer
from pl_api.permissions import IsOwnerOrReadOnly


class AccountList(generics.ListAPIView):
  """
  List all accounts
  """
  queryset = Account.objects.all()
  serializer_class = AccountSerializer


class AccountDetail(generics.RetrieveUpdateAPIView):
  """
  Retrieve or update an account if you're the owner
  """
  permission_classes = [IsOwnerOrReadOnly]
  queryset = Account.objects.all()
  serializer_class = AccountSerializer