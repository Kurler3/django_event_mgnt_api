from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken
# from django.conf import settings
from django.contrib.auth.models import User

class CookieJWTAuthentication(BaseAuthentication):

    # Override the authenticate function to use the access token from the cookies instead.
    def authenticate(self, request):
        
        # Get the access token from the cookies.
        access_token = request.COOKIES.get('access_token')

        # If the access token is not found, return None
        if not access_token:
            return None
        
        # Try to get the user from the access token.
        try:

            access_token_obj = AccessToken(token=access_token)

            # Get the user from the access token.
            user = self.get_user(access_token_obj)

            return (user, None)

        except Exception:
            return None
            # raise AuthenticationFailed('Invalid access token')

    # get_user function to get the user from the access token.
    def get_user(self, token):
        user_id = token['user_id']
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise AuthenticationFailed('No user found')


