from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=50, allow_null=True)
    age = serializers.IntegerField(min_value=0)
    class Meta:
        model = Profile
        fields = ('id', 'name', 'phone', 'age')
