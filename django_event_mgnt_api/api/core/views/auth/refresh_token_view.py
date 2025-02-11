
from rest_framework.views import APIView
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from ...utils.functions import get_user_from_raw_token
from rest_framework_simplejwt.tokens import RefreshToken
from ...permissions.not_authenticated_only import NotAuthenticatedOnly

class RefreshTokenView(APIView):

    permission_classes = [NotAuthenticatedOnly]

    def post(self, request):

        # Get the refresh token from the request
        refresh_token = request.COOKIES.get(
            settings.SIMPLE_JWT['REFRESH_TOKEN_COOKIE']
        )

        try:

            user = get_user_from_raw_token(
                token=refresh_token,
                is_access_token=False,
            )

            # Generate tokens for user.
            tokens = RefreshToken.for_user(user)

            response = Response({
                'status': status.HTTP_200_OK,
                'data': {
                    'message': 'Tokens refreshed'
                }
            })

            # Set the new tokens as http only cookies
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


            # Return response.
            return response

        except Exception as e:
            return Response(
                data={
                    'error': str(e),
                },
                status=status.HTTP_400_BAD_REQUEST
            )
