from rest_framework.views import APIView
from ....core.models import TicketModel
from ...serializers.tickets import TicketSerializer
from rest_framework.response import Response
from rest_framework import status

class ListEventTicketsView(APIView):

    def get(self, request, event_pk):

        # Query all tickets belonging to this user for this event.
        tickets = TicketModel.objects.filter(
            event=event_pk,
            user=request.user,
        ) 

        # Serialize it.
        serialized_tickets = TicketSerializer(
            tickets,
            many=True,
            context={ 'request': request }
        )

        # Return the serialized data.
        return Response(
            status=status.HTTP_200_OK,
            data=serialized_tickets.data
        )










