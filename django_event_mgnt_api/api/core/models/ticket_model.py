from django.db import models
from django.forms import ValidationError
from .event_model import EventModel
from django.contrib.auth.models import User

class TicketModel(models.Model):
    
    event = models.ForeignKey(to=EventModel, on_delete=models.CASCADE, related_name='tickets')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='tickets', db_index=True)

    quantity = models.IntegerField()

    # Price paid for all tickets.
    total = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='tickets_created')
    updated_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name='tickets_updated')
    code = models.CharField(max_length=50, unique=True, db_index=True)
    is_used = models.BooleanField(default=False)

    def clean(self):
        if self.quantity < 1:
            raise ValidationError('Quantity must be greater than 0')

    def __str__(self):
        return f'{self.event.title} - {self.user.username}'

    class Meta:
        db_table = 'ticket'
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets' 
