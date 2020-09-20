from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    m_contact = models.CharField(max_length=300)
    m_mobile = models.CharField(max_length=15)




class Hotel(models.Model):
    h_name = models.CharField(max_length=220)
    h_address = models.CharField(max_length=220)
    r_price = models.DecimalField(max_digits=11,decimal_places=2)
    hotel_rooms = models.IntegerField()
    h_image = models.ImageField(upload_to='Hotel images')
    h_country = models.CharField(max_length=220)
    h_mobile = models.CharField(max_length=20)
    h_location = models.CharField(max_length=220)

class Trip(models.Model):
    t_destination = models.CharField(max_length=250)
    t_price = models.DecimalField(max_digits=11, decimal_places=2)
    t_members = models.ManyToManyField(Member)
    T_country = models.CharField(max_length=220)
    created_at = models.DateTimeField(auto_now_add=True)
    start_at =  models.DateTimeField()
    end_at =  models.DateTimeField()
    t_mobile = models.CharField(max_length=20)
    t_location = models.CharField(max_length=220)
    t_image = models.ImageField(upload_to='trip images',null= True)
    



class Resturant(models.Model):
    r_name = models.CharField(max_length=220)
    r_address = models.CharField(max_length=220)
    r_image = models.ImageField(upload_to='Hotel images')
    r_menu_image =  models.ImageField(upload_to='menue images')
    r_country = models.CharField(max_length=220)
    created_at = models.DateTimeField(auto_now_add=True)
    open_at =  models.TimeField(null=True)
    close_at =  models.TimeField(null=True)
    r_mobile = models.CharField(max_length=20)
    t_location = models.CharField(max_length=220)


    

class Country(models.Model):
    c_name = models.CharField(max_length=220)
    c_hotels = models.ManyToManyField(Hotel)
    c_resturants = models.ManyToManyField(Resturant)
    c_trips = models.ManyToManyField(Trip)
    c_image = models.ImageField(upload_to='countries', null=True)



