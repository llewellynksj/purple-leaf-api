from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Account
from .serializers import AccountSerializer
from django.http import Http404


class AccountList(APIView):
  def get(self, request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)


class AccountDetail(APIView):
  def get_object(self, pk):
    try:
      account = Account.objects.get(pk=pk)
      return account
    except Account.DoesNotExist:
      raise Http404
  
  def get(self, request, pk):
    account = self.get_object(pk)
    serializer = AccountSerializer(account)
    return Response(serializer.data)
  