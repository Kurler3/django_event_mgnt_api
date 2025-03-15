from rest_framework.views import APIView
from ...serializers import TicketSerializer, PaymentSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from rest_framework.exceptions import APIException
from ....core import CustomAPIException

class BuyTicketsView(APIView):

    # @transaction.atomic
    def post(self, request):

        ctx = { 'request': request }

        with transaction.atomic():

            # Init the ticket serializer.
            ticket_serializer = TicketSerializer(
                data=request.data,
                context=ctx
            )

            if not ticket_serializer.is_valid():
                raise Exception({"error": ticket_serializer.errors})

            # Save the ticket
            ticket_serializer.save()

            # Init the payment serializer.
            payment_serializer = PaymentSerializer(  
                data={
                    'ticket': ticket_serializer.data['id'],
                    'amount': ticket_serializer.data['total'],
                },
                context=ctx
            )

            # Validate the payment serializer
            if not payment_serializer.is_valid():
                raise Exception(payment_serializer.errors)

            # Save the payment.
            payment_serializer.save()

            # Return to client the new ticket.
            return Response(
                data=ticket_serializer.data,
                status=status.HTTP_200_OK
            )

        