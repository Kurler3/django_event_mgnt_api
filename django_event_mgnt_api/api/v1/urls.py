from django.urls import path
from ..core import (
    RegisterView, 
    LoginView, 
    TestView
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

    #TODO - POST - /api/v1/auth/token/refresh (to refresh token)

    #TODO - POST - /api/v1/auth/logout (to logout)

    ##########################################
    ## EVENT ROUTES ##########################
    ##########################################

    #TODO - Event routes.

    
    ##########################################
    ## TICKET ROUTES #########################
    ##########################################


    #TODO - Ticket routes.

]
