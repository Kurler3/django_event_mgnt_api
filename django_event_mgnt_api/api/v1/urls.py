from django.urls import path
from ..core import (
    RegisterView, 
    LoginView, 
    TestView,
    RefreshTokenView,
    LogoutView,
)

from .views.events import (
    CreateEventView,
    UpdateEventView,
)

urlpatterns = [

    # GET - /api/v1/test (to test authentication middleware)
    path('test/', TestView.as_view(), name='test'),  # For testing

    #########################################
    ## AUTHENTICATION ROUTES ################
    #########################################

    # POST - /api/v1/auth/register
    path('auth/register/', RegisterView.as_view(), name='register'),  # For registration
    
    # POST - /api/v1/auth/login (to login)
    path('auth/login/', LoginView.as_view(), name="login"),

    # POST - /api/v1/auth/refresh
    path('auth/refresh/', RefreshTokenView.as_view(), name="refresh_token"),

    # POST - /api/v1/auth/logout (to logout)    
        #?? This route is open, because the tokens might be 
    path('auth/logout/', LogoutView.as_view(), name="logout"),

    ##########################################
    ## EVENT ROUTES ##########################
    ##########################################

    # Event routes.
    path('events/create', CreateEventView.as_view(), name='create_event'),
    path('events/update/<int:pk>', UpdateEventView.as_view(), name='update_event'),

    #TODO - Get event view
    

    #TODO - Delete event view

    #TODO - Get all events view (filter by owned events or all.)

    ##########################################
    ## TICKET ROUTES #########################
    ##########################################


    #TODO - Ticket routes.

]
