from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    # Define the inner Meta class with the fields that are going to be exposed.
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
        ]

