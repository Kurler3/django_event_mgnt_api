import django_filters
from ...models import PaymentModel

class PaymentFilter(django_filters.FilterSet):

    payment_date = django_filters.DateFilter(field_name='payment_date')

    class Meta:
        model = PaymentModel
        fields = ['payment_date']