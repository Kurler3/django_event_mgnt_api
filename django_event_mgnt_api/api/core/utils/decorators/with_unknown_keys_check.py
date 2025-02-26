from rest_framework.exceptions import ValidationError
from functools import wraps

def with_unknown_keys_check(serializer_class):

    original_validate_fn = serializer_class.validate

    @wraps(original_validate_fn)
    def new_validate_fn(self, data):

        if hasattr(self, 'initial_data'):

            # Check if there's any keys that do not exist.
            unknown_keys = set(self.initial_data.keys()) - set(self.fields.keys())
            if unknown_keys:
                raise ValidationError(f"Got unknown fields: {unknown_keys}")
            
            # Check if specifying read_only_fiels.
            for key in self.initial_data.keys():
                if key in self.Meta.read_only_fields:
                    raise ValidationError(f"Field '{key}' is read-only")

        return original_validate_fn(self, data)
    
    serializer_class.validate = new_validate_fn

    return serializer_class