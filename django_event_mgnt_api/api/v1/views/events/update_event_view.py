from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...serializers import EventSerializer
from ....core import (
    EventModel,
)
from ....core.permissions import EventOrganizerOnly
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class UpdateEventView(APIView):

    permission_classes = [IsAuthenticated, EventOrganizerOnly]

    def patch(self, request, pk):

        # Get the event object
        event = get_object_or_404(EventModel, pk=pk)

        # Check if the user is the organizer of the event
        self.check_object_permissions(request, event)  # Explicitly call permission check
        
        serializer = EventSerializer(
            instance=event, 
            data=request.data, 
            partial=True,
            context={'request': request}
        )
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)