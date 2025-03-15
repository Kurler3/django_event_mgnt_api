from rest_framework.views import APIView
from ....core.models import EventModel
from ...serializers.events import EventSerializer
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now

class ListEventsAttendingView(APIView):


    # Define the get method
    def get(self, request):
        
        # List tickets bought by user
        # tickets key on events model => then filtering on the user key on the tickets.
        user_events = EventModel.objects.filter(
            tickets__user=request.user,
            end_date__gte=now()
        ).distinct()

        # Pass the events through the serializer
        serialized_events = EventSerializer(
            user_events,
            many=True,
            context={ 'request': request }
        )

        # Return it to the client
        return Response(
            status= status.HTTP_200_OK,
            data=serialized_events.data
        )