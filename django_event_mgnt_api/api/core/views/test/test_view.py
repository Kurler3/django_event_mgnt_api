from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TestView(APIView):
    def get(self, request):
        return Response({
            'status': status.HTTP_200_OK,
            'data': {
                'message': 'Test view', 
                'user': request.user.username
            }
        })


