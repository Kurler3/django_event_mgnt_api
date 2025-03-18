from rest_framework.views import APIView
from ....core.models import PaymentModel
from ...serializers.payments import PaymentSerializer
from ....core import with_pagination, with_filtering, with_ordering, PaymentFilter

class ListPaymentsView(APIView):

    @with_pagination(serializer_class=PaymentSerializer)
    @with_ordering(allowed_fields=['payment_date'])
    @with_filtering(filtering_class=PaymentFilter, sendResponse=False)
    def get(self, request):
        return PaymentModel.objects.filter(user=request.user)
