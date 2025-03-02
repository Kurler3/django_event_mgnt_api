from django.core.exceptions import FieldDoesNotExist, BadRequest
from functools import wraps

def with_includes(serializer_class):

    original_init = serializer_class.__init__

    @wraps(original_init)
    def new_init(self, *args, **kwargs):

        # Get the context.
        ctx = kwargs.get('context', {})

        # Get request object
        request = ctx.get('request', None)

        includes = request.GET.get('includes', None) if request else None

        if includes:   

            # If no foreign key to serializer map => error
            if not hasattr(self, 'foreign_key_to_serializer_map'):
                raise BadRequest('Model serializer is missing map of foreign key to serializer')

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

        original_init(self, *args, **kwargs)
    

    serializer_class.__init__ = new_init

    return serializer_class

