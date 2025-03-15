from rest_framework.pagination import PageNumberPagination
from functools import wraps

def with_pagination(serializer_class):

    def decorator(view_func):

        @wraps(view_func)
        def wrapper(self, request, *args, **kwargs):

            # The view function using this decorator just needs to return the query set that needs to be paginated.
            queryset = view_func(self, request, *args, **kwargs)

            paginator = PageNumberPagination()

            result_page = paginator.paginate_queryset(queryset, request)

            serialized_data = serializer_class(
                result_page, 
                many=True, 
                context={'request': request}
            ).data

            return paginator.get_paginated_response(serialized_data)
        
        return wrapper

    return decorator