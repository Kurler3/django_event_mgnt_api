from rest_framework.views import APIView
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

# Custom logout view, because will delete access token and refresh token cookies.
# By default, all routes are protected, so 
class LogoutView(APIView):

    def post(self, request):

        response = Response(
            data={
                'message': 'Logout successful'
            },
            status=status.HTTP_200_OK
        )

        response.delete_cookie(settings.SIMPLE_JWT['ACCESS_TOKEN_COOKIE'])
        response.delete_cookie(settings.SIMPLE_JWT['REFRESH_TOKEN_COOKIE'])

        return response


