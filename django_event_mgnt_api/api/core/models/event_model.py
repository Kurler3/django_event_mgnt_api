
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class EventModel(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    organizer = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='events')
    max_attendees = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='events_created')
    updated_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name='events_updated')

    def __str__(self):
        return self.title

    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError('End date cannot be before start date')

    class Meta:
        db_table = 'event'
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
