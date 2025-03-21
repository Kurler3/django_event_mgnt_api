from django.db import models
from django.contrib.auth.models import User
from .ticket_model import TicketModel
from .event_model import EventModel
from django.forms import ValidationError

class PaymentModel(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='payments', db_index=True)

    ticket = models.ForeignKey(to=TicketModel, on_delete=models.CASCADE, related_name='ticket_payment', db_index=True)
    
    event = models.ForeignKey(to=EventModel, on_delete=models.CASCADE, related_name='event_payment', db_index=True)

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
     
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='payments_created')

    def __str__(self):
        return f'{self.user.username} - {self.amount}'

    def clean(self):
        if self.amount <= 0:
            raise ValidationError('Amount paid must not be smaller or equal to 0')

    class Meta:
        db_table = 'payment'
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'