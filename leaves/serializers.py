from rest_framework import serializers
from .models import Leaf


class LeafSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')
  is_owner = serializers.SerializerMethodField()
  