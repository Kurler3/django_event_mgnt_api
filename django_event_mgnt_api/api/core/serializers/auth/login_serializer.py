from rest_framework import serializers
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    
    username = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(max_length=100, write_only=True, required=True)

    def validate(self, data):
        user = authenticate(**data)
        if not user or not user.is_active:
            raise serializers.ValidationError('Invalid credentials')
        return user