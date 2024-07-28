from rest_framework import serializers
from .models import Leaf


class LeafSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')
  is_owner = serializers.SerializerMethodField()
  account_id = serializers.ReadOnlyField(source='owner.account.id')
  account_image = serializers.ReadOnlyField(source='owner.account.image.url')

  def validate_image(self, value):
    if value.size > 2 * 1024 * 1024:
        raise serializers.ValidationError('Image too large - file should be less than 2MB')
    if value.image.height > 4096:
        raise serializers.ValidationError(
            'Image too large - image height should be no larger than 4096px'
        )
    if value.image.width > 4096:
        raise serializers.ValidationError(
            'Image too large - image width should be no larger than 4096px'
        )
    return value

  def get_is_owner(self, obj):
    request = self.context['request']
    return request.user == obj.owner
  
  class Meta:
    model = Leaf
    fields = [
      'id', 'owner', 'created_at', 'updated_at', 'loss_type', 'name', 'parent_name1', 'parent_name2', 'dob_due_date', 'weight', 'image', 'memory', 'is_owner', 'account_id', 'account_image'
    ]