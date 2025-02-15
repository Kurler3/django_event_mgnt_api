from ...serializers import EventSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CreateEventView(APIView):

    def post(self, request):
        serializer = EventSerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
