from rest_framework.views import APIView
from ...serializers.auth.login_serializer import LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from ...permissions.not_authenticated_only import NotAuthenticatedOnly

# Custom login view, because will set access token and refresh token as http only cookies.
class LoginView(APIView):

    # Opens up the route to users that are not authenticated ONLY
    permission_classes = [NotAuthenticatedOnly]

    def post(self, request):

        serializer = LoginSerializer(data=request.data)

        # Generate tokens
        if serializer.is_valid():
            
            user = serializer.validated_data

            # Generate tokens for user.
            tokens = RefreshToken.for_user(user)

            # Set access token as http only cookie.
            response = Response({
                'status': status.HTTP_200_OK,
                'data': {
                    'message': 'Login successful',
                    'user': user.username
                }
            })

            # Set access token as http only cookie.
            response.set_cookie(
                key=settings.SIMPLE_JWT['ACCESS_TOKEN_COOKIE'],
                value=str(tokens.access_token),
                httponly=True,
                secure=True,
                samesite='Strict', # Only send cookies if the request is coming from the same origin.
            )

            # Set refresh token as http only cookie.
            response.set_cookie(
                key=settings.SIMPLE_JWT['REFRESH_TOKEN_COOKIE'],
                value=tokens,
                httponly=True,
                secure=True,
                samesite='Strict', # Only send cookies if the request is coming from the same origin.
            )

            return response

        # Return error if serializer is not valid.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
