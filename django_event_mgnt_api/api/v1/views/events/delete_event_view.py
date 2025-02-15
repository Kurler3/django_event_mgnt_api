from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from ....core import (
    EventOrganizerOnly,
    EventModel
)
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

class DeleteEventView(APIView):
    def delete(self, request, pk):

        # Get the event
        event = get_object_or_404(EventModel, pk=pk)

        # Run object permission check.
        self.check_object_permissions(request, event)

        # Delete the event.
        event.delete()

        # Return msg to client.
        return Response(
            status=status.HTTP_200_OK,
            data={
                'message': 'Event deleted successfully!'
            }
        )
