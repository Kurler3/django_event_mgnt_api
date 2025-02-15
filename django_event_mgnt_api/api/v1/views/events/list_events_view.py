from rest_framework.views import APIView
from ....core import EventModel
from ...serializers import EventSerializer
from rest_framework.response import Response
from rest_framework import status

class ListEventsView(APIView):

    # Get all events (public)
    def get(self, request):
        
        events = EventModel.objects.all()
        
        serialized_data =  EventSerializer(events, many=True).data

        return Response(
            status=status.HTTP_200_OK,
            data=serialized_data
        )
