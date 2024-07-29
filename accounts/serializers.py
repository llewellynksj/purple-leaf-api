from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
  """
  Serialixer linked to Account model
  """
  user = serializers.ReadOnlyField(source='user.username')
  is_user = serializers.SerializerMethodField()
  leaf_count = serializers.ReadOnlyField()

  def get_is_user(self, obj):
      request = self.context['request']
      return request.user == obj.user

  class Meta:
    model = Account
    fields = [
      'id', 'user', 'is_user', 'created_at', 'updated_at', 'name', 'image', 'leaf_count',
    ]