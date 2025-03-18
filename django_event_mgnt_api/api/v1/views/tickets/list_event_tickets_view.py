from rest_framework.views import APIView
from ....core.models import TicketModel
from ...serializers.tickets import TicketSerializer
from ....core import with_pagination, with_filtering, with_ordering, TicketFilter

class ListEventTicketsView(APIView):

    @with_pagination(serializer_class=TicketSerializer)
    @with_ordering(allowed_fields=['purchase_date'])
    @with_filtering(filtering_class=TicketFilter, sendResponse=False)
    def get(self, request, event_pk):
        # Query all tickets belonging to this user for this event.
        return TicketModel.objects.filter(
            event=event_pk,
            user=request.user,
        ) 







