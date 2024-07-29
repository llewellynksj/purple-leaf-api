from rest_framework import serializers
from .models import Leaf
from remember.models import Remember


class LeafSerializer(serializers.ModelSerializer):
  """
  Serializer linked to the Leaf model
  """
  user = serializers.ReadOnlyField(source='user.username')
  is_user = serializers.SerializerMethodField()
  account_id = serializers.ReadOnlyField(source='user.account.id')
  account_image = serializers.ReadOnlyField(source='user.account.image.url')
  remember_id = serializers.SerializerMethodField()

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

  def get_is_user(self, obj):
    request = self.context['request']
    return request.user == obj.user
  
  def get_remember_id(self, obj):
    user = self.context['request'].user
    if user.is_authenticated:
      remember = Remember.objects.filter(
        user=user, leaf=obj
      ).first()
      return remember.id if remember else None
    return None
  
  class Meta:
    model = Leaf
    fields = [
      'id', 'user', 'created_at', 'updated_at', 'loss_type', 'name', 'parent_name1', 'parent_name2', 'dob_due_date', 'weight', 'image', 'memory', 'is_user', 'account_id', 'account_image', 'remember_id'
    ]