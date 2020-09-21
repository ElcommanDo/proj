from django.contrib import admin
from .models import Country, Hotel, Member, Resturant, Trip, resturant_reservations, trip_reservations, Hotel_reservations
# Register your models here.
admin.site.register([Country, Hotel, Member, Resturant, Trip,resturant_reservations, trip_reservations, Hotel_reservations])
