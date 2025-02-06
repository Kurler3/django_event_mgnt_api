from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from ..core import RegisterView

urlpatterns = [

    # POST - /api/v1/auth/register
    path('auth/register/', RegisterView.as_view(), name='register'),  # For registration


    #TODO - Substitute the auth/token and auth/token/refresh with the custom login and refresh token views

    # path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # For login (obtain JWT)
    # path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # For refreshing the token



    #TODO - Event routes.

    #TODO - Ticket routes.

]
