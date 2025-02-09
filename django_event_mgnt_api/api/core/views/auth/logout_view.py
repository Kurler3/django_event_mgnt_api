from rest_framework.views import APIView

# Custom logout view, because will delete access token and refresh token cookies.
# By default, all routes are protected, so 
class LogoutView(APIView):

    def post(self, request):

        # Set header to delete the access token cookie and the refresh token cookie as well.

        # Blacklist both JWTs.

        pass


