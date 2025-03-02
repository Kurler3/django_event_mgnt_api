from rest_framework.views import APIView
from ....core.models import TicketModel
from rest_framework import status
from rest_framework.response import Response
from ...serializers.tickets import TicketSerializer

class UseTicketView(APIView):

    def post(self, request, code):

        # Get the ticket
        ticket = TicketModel.objects.get(code=code)

        if not ticket:
            return Response(
                status=400,
                data={'message': 'Couldn\'nt find ticket with this code'}
            )

        # If the ticket is already used => error
        if ticket.is_used:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={ 'message': 'This ticket has already been used!' }
            )

        ticket_serializer = TicketSerializer(
            instance=ticket,
            data={'is_used': True},
            partial=True,
            context={'request': request}
        )

        if not ticket_serializer.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=ticket_serializer.errors
            )

        ticket_serializer.save()

        return Response(
            status=status.HTTP_200_OK,
            data={ 'message': 'This ticket has been used successfully!'}
        )