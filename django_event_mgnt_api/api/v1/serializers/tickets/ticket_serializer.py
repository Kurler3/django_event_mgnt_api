from rest_framework import serializers
from ....core.models import TicketModel, EventModel
from uuid import uuid4
from ....core.utils.decorators import (
    with_includes,
    with_unknown_keys_check
)
from django.db.models import Sum
from rest_framework.exceptions import ValidationError


@with_includes
@with_unknown_keys_check
class TicketSerializer(serializers.ModelSerializer):

    class Meta:

        model = TicketModel

        fields = '__all__'

        read_only_fields = [
            'user',
            'total',
            'updated_at',
            'updated_by',
            'created_at',
            'created_by',
            'code',
            'is_used'
        ]

    # If creating
        # - Need to set user.
        # - Need to set total by using the event.price_per_ticket * ticket.quantity.
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['created_by'] = user
        validated_data['updated_by'] = user
        validated_data['user'] = user

        # Init random code
        validated_data['code'] = uuid4()

        validated_data['total'] = validated_data['event'].price_per_ticket * validated_data['quantity']

        return super().create(validated_data)

    def update(self, instance, validated_data):

        validated_data['updated_by'] = self.context['request'].user

        return super().update(instance, validated_data)

    def validate(self, data):

        if hasattr(self, 'initial_data') and 'event' in self.initial_data and self.instance and 'quantity' in self.initial_data:

            # Check if event exists.
            if not EventModel.objects.get(pk=self.initial_data['event']):
                raise ValidationError('Event specified doesn\'t exist')

            # Get all the sum of tickets already bought for this event
            total_tickets_bought = TicketModel.objects.filter(event=self.initial_data['event']).aaggregate(
                total=Sum('quantity')
            )

            if total_tickets_bought + self.initial_data['quantity'] > self.initial_data['event'].max_attendees:
                raise ValidationError(
                    'Trying to buy more tickets than event allows')
            
        return data
