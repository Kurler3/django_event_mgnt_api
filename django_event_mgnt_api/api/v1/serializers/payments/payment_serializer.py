from rest_framework import serializers
from ....core.utils.decorators import (
    with_includes,
    with_unknown_keys_check
)
from ....core.models import PaymentModel
from ...serializers.tickets import TicketSerializer
from ...serializers.events import EventSerializer
from ...serializers.user import UserSerializer

@with_includes
@with_unknown_keys_check
class PaymentSerializer(serializers.ModelSerializer):

    foreign_key_to_serializer_map = {
        'event': EventSerializer,
        'user': UserSerializer,
        'ticket': TicketSerializer,
        'created_by': UserSerializer,
    }

    class Meta:
        model = PaymentModel    
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['event'] = validated_data['ticket'].event
        validated_data['created_by'] = user
        validated_data['user'] = user
        return super().create(validated_data)