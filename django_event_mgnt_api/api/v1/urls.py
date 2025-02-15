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
    GetEventView,
    DeleteEventView,
    ListEventsView,
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
    path('events/<int:pk>', GetEventView.as_view(), name='get_event'),
    path('events/delete/<int:pk>', DeleteEventView.as_view(), name='delete_event'),
    path('events/list', ListEventsView.as_view(), name='list_events'),

    ##########################################
    ## TICKET ROUTES #########################
    ##########################################


    #TODO - Ticket routes.


]
