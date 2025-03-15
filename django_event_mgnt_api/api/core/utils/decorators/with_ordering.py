from functools import wraps
from ..classes import CustomAPIException
from rest_framework import status

def with_ordering(default_ordering='-id', allowed_fields=None):
    
    def decorator(view_func):
        
        @wraps(view_func)
        def wrapper(self, request, *args, **kwargs):

            # Get the query set.
            query_set = view_func(self, request, *args, **kwargs)

            # Get optional ordering
            optional_ordering = request.GET.get('ordering', None)

            # If specified a custom ordering field AND allowed fields AND the ordering param is not inside it, then
            if optional_ordering:
                
                # If there's no allowed fields
                if not allowed_fields:
                    raise CustomAPIException(
                        detail='No allowed optional fields for ordering defined',
                        status_code=status.HTTP_400_BAD_REQUEST
                    )

                # Check if the optional ordering is inside the allowed fields.
                if optional_ordering.lstrip('-+') not in allowed_fields:
                    raise CustomAPIException(
                        detail=f'Ordering by the field {optional_ordering} is not allowed. These are the allowed fields to order by: {", ".join(allowed_fields)}',
                        status_code=status.HTTP_400_BAD_REQUEST
                    ) 

            # Get the actual ordering
            ordering = optional_ordering or default_ordering

            # Order the query set.
            return query_set.order_by(ordering)
        return wrapper        
    return decorator
