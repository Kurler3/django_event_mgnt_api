
from rest_framework.views import APIView
from rest_framework.response import Response

class ExampleV1View(APIView):
    def get(self, request):
        response = Response({"message": "This is API v1"})
        response['X-API-Warning'] = 'This version will be deprecated soon, please upgrade to v2.'
        return response