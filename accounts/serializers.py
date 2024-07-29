from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
  """
  Serialixer linked to Account model
  """
  user = serializers.ReadOnlyField(source='user.username')
  is_owner = serializers.SerializerMethodField()

  def get_is_owner(self, obj):
      request = self.context['request']
      return request.user == obj.user

  class Meta:
    model = Account
    fields = [
      'id', 'user', 'is_owner', 'created_at', 'updated_at', 'name', 'image',
    ]