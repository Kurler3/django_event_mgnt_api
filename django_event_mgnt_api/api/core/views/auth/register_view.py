from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from ...serializers.auth.register_serializer import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status

class RegisterView(APIView):

    permission_classes = [AllowAny]

    # POST /api/auth/register
    def post(self, request):
        
        # Serialize the request data
        serializer = RegisterSerializer(data=request.data)

        # Validate the data
        if serializer.is_valid():
            
            # Create a new user
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

