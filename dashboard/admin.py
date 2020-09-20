from django.contrib import admin
from .models import Country, Hotel, Member, Resturant, Trip
# Register your models here.
admin.site.register([Country, Hotel, Member, Resturant, Trip])
