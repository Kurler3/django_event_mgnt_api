from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):

    # Make sure the field is not visible in the response
    password = serializers.CharField(max_length=100, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']
    
    # Validate the username (check if it already exists)
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Username already exists') 
        return value

    # Create a new user
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    