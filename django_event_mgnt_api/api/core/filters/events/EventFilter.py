
import django_filters
from ...models import EventModel

class EventFilter(django_filters.FilterSet):

    category = django_filters.CharFilter(field_name="category", lookup_expr="icontains")
    start_date = django_filters.DateFilter(field_name="start_date")
    location = django_filters.CharFilter(field_name="location", lookup_expr="icontains")

    class Meta:
        model = EventModel
        fields = ["category", "start_date"]
