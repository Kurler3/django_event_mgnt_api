from rest_framework.views import APIView
from rest_framework.response import Response

class ExampleV2View(APIView):
    def get(self, request):
        return Response({"message": "This is API v2"})

