from django.urls import path
from ..core import (
    RegisterView, 
    LoginView, 
    TestView,
    RefreshTokenView,
    LogoutView,
)

urlpatterns = [

    # GET - /api/v1/test (to test authentication middleware)
    path('test/', TestView.as_view(), name='test'),  # For testing


    #########################################
    ## AUTHENTICATION ROUTES ################
    #########################################

    # POST - /api/v1/auth/register
    path('auth/register/', RegisterView.as_view(), name='register'),  # For registration
    
    # POST - /api/v1/auth/token (to login)
    path('auth/token/', LoginView.as_view(), name="login"),

    # POST - /api/v1/auth/token/refresh
    path('auth/token/refresh/', RefreshTokenView.as_view(), name="refresh_token"),

    # POST - /api/v1/auth/logout (to logout)
    path('auth/logout/', LogoutView.as_view(), name="logout"),

    ##########################################
    ## EVENT ROUTES ##########################
    ##########################################

    #TODO - Event routes.

    
    ##########################################
    ## TICKET ROUTES #########################
    ##########################################


    #TODO - Ticket routes.

]
