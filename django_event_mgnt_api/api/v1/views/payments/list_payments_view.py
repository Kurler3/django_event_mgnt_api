from rest_framework.views import APIView
from ....core.models import PaymentModel
from ...serializers.payments import PaymentSerializer
from rest_framework.response import Response
from rest_framework import status
from ....core import with_pagination

class ListPaymentsView(APIView):

    @with_pagination(serializer_class=PaymentSerializer)
    def get(self, request):
        return PaymentModel.objects.filter(user=request.user)
