from rest_framework.permissions import BasePermission
from django.conf import settings

class NotAuthenticatedOnly(BasePermission):
    
    def has_permission(self, request, view):
        
        has_access_token = request.COOKIES.get(
            settings.SIMPLE_JWT['ACCESS_TOKEN_COOKIE']
        ) is not None

        # If user has access token, then they are authenticated.
        if has_access_token:
            return False

        return True

