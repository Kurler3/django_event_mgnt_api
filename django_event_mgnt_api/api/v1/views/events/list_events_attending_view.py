from rest_framework.views import APIView
from ....core.models import EventModel
from ...serializers.events import EventSerializer
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now
from ....core import EventFilter, with_pagination, with_filtering, with_ordering

class ListEventsAttendingView(APIView):
    # Define the get method

    @with_pagination(serializer_class=EventSerializer)
    @with_ordering(allowed_fields=['start_date', 'end_date'])
    @with_filtering(filtering_class=EventFilter, sendResponse=False)
    def get(self, request):
        # List tickets bought by user
        # tickets key on events model => then filtering on the user key on the tickets.
        return EventModel.objects.filter(
            tickets__user=request.user,
            end_date__gte=now()
        ).distinct()