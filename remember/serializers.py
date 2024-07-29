from rest_framework import serializers
from remember.models import Remember


class RememberSerializer(serializers.ModelSerializer):
    """
    Serializer for the Remember model
    """
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Remember
        fields = ['id', 'created_at', 'user', 'leaf']