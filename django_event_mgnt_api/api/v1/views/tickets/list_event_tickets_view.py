from rest_framework.views import APIView
from ....core.models import TicketModel
from ...serializers.tickets import TicketSerializer
from ....core import with_pagination

class ListEventTicketsView(APIView):

    @with_pagination(serializer_class=TicketSerializer)
    def get(self, request, event_pk):
        # Query all tickets belonging to this user for this event.
        return TicketModel.objects.filter(
            event=event_pk,
            user=request.user,
        ) 









