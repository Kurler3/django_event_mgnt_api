from rest_framework import serializers
from ....core.models import EventModel, TicketModel
from rest_framework.exceptions import ValidationError
from django.db.models import Sum
from ..user.user_serializer import UserSerializer
from django.core.exceptions import FieldDoesNotExist, BadRequest

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

    # Override the constructor.
    def __init__(self, *args, **kwargs):

        # Get the context.
        ctx = kwargs.get('context', {})

        # Get request object
        request = ctx.get('request', None)

        includes = request.GET.get('includes', None) if request else None

        if includes:   

            # Split the includes properly to get an array of attributes to include.
            # Also removes empty keys.
            includes = [x for x in includes.replace(" ", "").replace("\t", "").replace("\n", "").split(',') if x.strip()]

            # Get ForeignKey fields dynamically
            foreign_keys = set([field.name for field in self.Meta.model._meta.fields if field.get_internal_type() == "ForeignKey"])
            fields = set(self.fields.keys())

            # Check that there isn't any key in the includes that doesn't exist OR that is not a foreign key.
            for includedKey in includes:

                # If not in the schema at all => error
                if includedKey not in fields:
                    raise FieldDoesNotExist(f'The field {includedKey} doesn\'t exist.')
            
                if includedKey not in foreign_keys:
                    raise BadRequest(f'The field {includedKey} isn\'t a foreign key.')

                # There needs to be a serializer to map the attribute to!
                if includedKey not in self.foreign_key_to_serializer_map:
                    raise BadRequest(f'The field {includedKey} doesn\'t have a serializer defined.')

            # For each included key, call the mapped serializer class!
            for includedKey in includes:
                self.fields[includedKey] = self.foreign_key_to_serializer_map[includedKey]()

        super().__init__(*args, **kwargs)

    
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

            # Check if there's any keys that do not exist.
            unknown_keys = set(self.initial_data.keys()) - set(self.fields.keys())
            if unknown_keys:
                raise ValidationError(f"Got unknown fields: {unknown_keys}")
            
            # Check if specifying read_only_fiels.
            for key in self.initial_data.keys():
                if key in self.Meta.read_only_fields:
                    raise ValidationError(f"Field '{key}' is read-only")
            
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