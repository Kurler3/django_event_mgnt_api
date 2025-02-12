from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...serializers import EventSerializer
from ....core.models import EventModel

class UpdateEventView(APIView):
    def put(self, request, pk):

        # Get the event object
        event = EventModel.objects.get(pk=pk)

        # Check if the user is the organizer of the event
        if event.organizer != request.user:
            
            return Response(
                {
                    'error': 'You are not the organizer of this event'
                }, 
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = EventSerializer(event, data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)