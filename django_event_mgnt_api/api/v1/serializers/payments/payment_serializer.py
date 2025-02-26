from rest_framework import serializers
from ....core.utils.decorators import (
    with_includes,
    with_unknown_keys_check
)
from ....core.models import PaymentModel

@with_includes
@with_unknown_keys_check
class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentModel    

        fields = [
            'ticket',
            'amount',
        ]

    def create(self, validated_data):

        user = self.context['request'].user

        validated_data['event'] = validated_data['ticket'].event
        validated_data['created_by'] = user
        validated_data['user'] = user

        return super().create(validated_data)