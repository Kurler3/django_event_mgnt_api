from rest_framework.exceptions import APIException
from rest_framework import status

class CustomAPIException(APIException):

    def __init__(self, detail, code="error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR):
        
        # Call the API Exception constructor first (it sets the status_code to 500) 
        super().__init__(detail=detail, code=code)

        if status_code:
            self.status_code = status_code
        
