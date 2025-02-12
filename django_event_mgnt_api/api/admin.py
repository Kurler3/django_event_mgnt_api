from django.contrib import admin
from .core import (
    EventModel,
    PaymentModel,
    TicketModel,
)

# Register your models here.
admin.register(EventModel)
admin.register(PaymentModel)
admin.register(TicketModel)