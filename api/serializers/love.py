from rest_framework import serializers
from ..models.love import Love
from .user import UserSerializer

class LoveSerializer(serializers.ModelSerializer):
    # user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Love
        fields = ('id', 'user', 'one', 'two', 'three', 'four', 'five')

