from functools import wraps
from rest_framework.response import Response
from rest_framework import status

def with_filtering(filtering_class, sendResponse=False):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(self, request, *args, **kwargs):
            
            query_set = view_func(self, request, *args, **kwargs)
            
            filtered_queryset = filtering_class(request.GET, queryset=query_set).qs

            if sendResponse:
                return Response(
                    status=status.HTTP_200_OK,
                    data=filtered_queryset
                )
            
            return filtered_queryset
        return wrapper
    return decorator