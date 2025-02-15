from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...serializers import EventSerializer
from ....core import EventModel
from django.shortcuts import get_object_or_404

class GetEventView(APIView):
    
    def get(self, request, pk):

        event = get_object_or_404(EventModel, pk=pk)

        # Serialize the event
        serializer = EventSerializer(event)

        # Return the event.
        return Response({
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })



