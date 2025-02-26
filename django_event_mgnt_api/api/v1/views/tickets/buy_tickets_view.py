from rest_framework.views import APIView
from ...serializers import TicketSerializer, PaymentSerializer
from rest_framework.response import Response
from rest_framework import status

class BuyTicketsView(APIView):

    #TODO - Need to put this in a transaction.
    def post(self, request):

        ctx = { 'request': request }

        # Init the ticket serializer.
        ticket_serializer = TicketSerializer(
            data=request.data,
            context=ctx
        )

        if not ticket_serializer.is_valid():
            return Response(
                data=ticket_serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )

        # Save the ticket
        ticket_serializer.save()

        amount_paid = ticket_serializer.data['quantity'] * ticket_serializer.data['event'].price_per_ticket

        # Init the payment serializer.
        payment_serializer = PaymentSerializer(
            data={
                'ticket': ticket_serializer.data,
                'amount': amount_paid
            },
            context=ctx
        )

        # Validate the payment serializer
        if not payment_serializer.is_valid():
            return Response(
                data=payment_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        # Save the payment.
        payment_serializer.save()

        # Return to client the new ticket.
        return Response(
            data=ticket_serializer.data,
            status=status.HTTP_200_OK
        )