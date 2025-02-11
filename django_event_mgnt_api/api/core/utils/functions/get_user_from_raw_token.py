from rest_framework_simplejwt.tokens import (
    AccessToken,
    RefreshToken,
)
from django.contrib.auth.models import User

def get_user_from_raw_token(
        token,
        is_access_token=True,
):
    
    try:

        if not token:
            raise Exception('No token provided')

        token_obj =  AccessToken(token) if is_access_token else RefreshToken(token)

        user_id = token_obj['user_id']

        if not user_id:
            raise Exception('Invalid token')

        user = User.objects.get(id=user_id)         

        if not user:
            raise Exception('No user found')
    
        return user
    
    except User.DoesNotExist:
        raise Exception('No user found')
    except Exception as e:
        raise Exception(e)

