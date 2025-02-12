from rest_framework import serializers
from ....core.models import EventModel

class EventSerializer(serializers.ModelSerializer):

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
    
