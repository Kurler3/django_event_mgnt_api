from rest_framework.views import APIView
from ....core.models import PaymentModel
from ...serializers.payments import PaymentSerializer
from rest_framework.response import Response
from rest_framework import status

class ListPaymentsView(APIView):

    def get(self, request):

        payments = PaymentModel.objects.filter(user=request.user)

        payments_serializer = PaymentSerializer(
            payments,
            many=True,
            context={'request': request}
        )

        return Response(
            status=status.HTTP_200_OK,
            data=payments_serializer.data,
        )

