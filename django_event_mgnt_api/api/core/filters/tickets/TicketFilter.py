import django_filters

from ...models import TicketModel

class TicketFilter(django_filters.FilterSet):

    total = django_filters.NumberFilter(field_name='total')
    is_used = django_filters.BooleanFilter(field_name='is_used')
    purchase_date = django_filters.DateFilter(field_name='purchase_date')

    class Meta:
        model = TicketModel

        fields = [
            'total',
            'is_used',
            'purchase_date'
        ]


