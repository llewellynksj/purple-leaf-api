from rest_framework import serializers
from .models import Leaf


class LeafSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')
  is_owner = serializers.SerializerMethodField()
  account_id = serializers.ReadOnlyField(source='owner.account.id')
  account_image = serializers.ReadOnlyField(source='owner.account.image.url')

  def get_is_owner(self, obj):
    request = self.context['request']
    return request.user == obj.owner
  
  class Meta:
    model = Leaf
    fields = [
      'id', 'owner', 'created_at', 'updated_at', 'loss_type', 'name', 'parent_name1', 'parent_name2', 'dob_due_date', 'weight', 'image', 'memory'
    ]