from rest_framework.views import APIView
from ....core import EventModel, with_pagination, EventFilter, with_filtering, with_ordering
from ...serializers import EventSerializer


class ListEventsView(APIView):

    @with_pagination(EventSerializer)
    @with_ordering(allowed_fields=['start_date', 'end_date'])
    @with_filtering(filtering_class=EventFilter, sendResponse=False)
    def get(self, request):
        return EventModel.objects.all()
