from django.urls import path
from .views.example import ExampleV1View
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # For login (obtain JWT)
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # For refreshing the token


    # Event routes.

    # Ticket routes.

]
