from django.contrib import admin
from .core import (
    EventModel,
    PaymentModel,
    TicketModel,
)

# Register your models here.
admin.site.register(EventModel)
admin.site.register(PaymentModel)
admin.site.register(TicketModel)