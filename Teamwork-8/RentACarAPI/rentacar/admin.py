from django.contrib import admin
from .models import Car, Customer, Reservation, Query

admin.site.register(Car)
admin.site.register(Customer)
admin.site.register(Reservation)
admin.site.register(Query)