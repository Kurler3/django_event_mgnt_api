from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

class EventOrganizerOnly(BasePermission):
    # Check if the user is the organizer of the event by using this function which is called by the view AFTER getting the event object.
    def has_object_permission(self, request, view, obj):        
        if obj.organizer != request.user:
            raise PermissionDenied('You are not the organizer of this event')
        return True
