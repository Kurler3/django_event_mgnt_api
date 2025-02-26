from rest_framework import serializers
from ....core.models import EventModel, TicketModel
from rest_framework.exceptions import ValidationError
from django.db.models import Sum
from ..user.user_serializer import UserSerializer
from ....core.utils.decorators import with_includes, with_unknown_keys_check

@with_includes
@with_unknown_keys_check
class EventSerializer(serializers.ModelSerializer):
    
    foreign_key_to_serializer_map = {
        'organizer': UserSerializer,
        'created_by': UserSerializer,
        'updated_by': UserSerializer
    }

    class Meta:
        model = EventModel
        fields = '__all__'
        
        # User can't override these!
        read_only_fields = [
            'created_by', 
            'updated_by',
            'created_at',
            'updated_at', 
            'organizer'
        ]
    
    # Override the create method to set the created_by and organizer fields to the current user without having to explicitly do it in the view.
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['created_by'] = user
        validated_data['updated_by'] = user
        validated_data['organizer'] = user
        return super().create(validated_data)

    # Override the update method to set the updated_by field to the current user without having to explicitly do it in the view.
    def update(self, instance, validated_data):

        # Check if the new start date (if updating it) is BEFORE the previous startDate
        if 'start_date' in validated_data and validated_data['start_date'] < instance.start_date:
            raise serializers.ValidationError('Start date cannot be before the previous start date')

        # Set the updated_by field to the current user
        validated_data['updated_by'] = self.context['request'].user

        # Call the parent class's update method
        return super().update(instance, validated_data)
    

    # Override the validate method to check for unknown fields in the request data.
    def validate(self, data):

        if hasattr(self, 'initial_data'):
            
            # Check if the new max attendees is lower than the total tickets already bought.
            if 'max_attendees' in self.initial_data and self.instance:
                old_max_attendees = self.instance.max_attendees  # Access model field directly
                new_max_attendees = self.initial_data['max_attendees']

                if not isinstance(new_max_attendees, int):
                    raise ValidationError('Max attendees must be an integer') 

                # Only check if the new max is lower than the current max
                if old_max_attendees > new_max_attendees:

                    # Aggregate sum of ticket quantities directly in the database
                    total_tickets_bought = TicketModel.objects.filter(event=self.instance).aggregate(
                        total=Sum('quantity')
                    )['total'] or 0  # Default to 0 if no tickets exist

                    if total_tickets_bought > new_max_attendees:
                        raise ValidationError('Cannot set max attendees to a number lower than the total tickets already bought')
                    
        return data