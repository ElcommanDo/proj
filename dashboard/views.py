from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import models
from .models import Hotel_reservations, resturant_reservations, trip_reservations, Member
from django.core.mail import send_mail
# Create your views here.


def login_admin(request):
    if request.method == "POST":
        cd = request.POST
        user = authenticate(request, username=cd['username'], password=cd['password'])
        if user:
            login(request, user)
            return redirect('adminstration')
        else:
            messages.warning(request, 'username does not exist')
            return redirect('home')


@login_required(login_url='home')
def adminstration(request):
    countries = models.Country.objects.all()
    return render(request, 'dash/admin.html', {'countries':countries})



def logout_admin(request):
    logout(request)
    messages.success(request, 'logout has made successfully')
    return redirect('home')
    


def add_hotel(request):
    if request.method =="POST":
        cd = request.POST
        if models.Hotel.objects.filter(h_name=cd['h_name']):
            messages.warning(request, 'hotel has added before')
            return redirect('adminstration')
        hotel = models.Hotel()
        hotel.h_name, hotel.h_address, hotel.h_location = cd['h_name'], cd['h_address'], cd['h_location']
        hotel.hotel_rooms, hotel.h_mobile, hotel.h_country = cd['hotel_rooms'], cd['h_mobile'], cd['h_country'] 
        hotel.h_image = request.FILES.get("h_image")
        hotel.r_price = cd['r_price']
        hotel.save()
        c = models.Country.objects.get(c_name=cd['t_country'])
        c.c_hotels.add(trip)
        messages.success(request, 'hotel has added successfully')
        return redirect('adminstration')



def add_trip(request):
    if request.method =="POST":
        cd = request.POST
        if models.Trip.objects.filter(t_destination=cd['t_destination']):
            messages.warning(request, 'trip has added before')
            return redirect('adminstration')
        trip = models.Trip()
        trip.t_destination = cd['t_destination']
        trip.t_price = cd['t_price']
        trip.T_country = cd['t_country']
        trip.start_at =  cd['start_at']
        trip.end_at =  cd['end_at']
        trip.t_mobile =cd['t_mobile']
        trip.t_location =cd['t_location']
        trip.t_image = request.FILES.get("t_image")
        trip.save()
        c = models.Country.objects.get(c_name=cd['t_country'])
        c.c_trips.add(trip)
        c.save()

        messages.success(request, 'the trip has added successfully')
        return redirect('adminstration')



def add_resturant(request):

  if request.method =="POST":
        cd = request.POST
        if models.Resturant.objects.filter(r_name=cd['r_name']):
            messages.warning(request, 'Resturant has added before')
            return redirect('adminstration')
        resturant = models.Resturant()
        
        resturant.r_name = cd['r_name']
        resturant.r_address =  cd['r_address']
        resturant.r_image = request.FILES.get('r_image')
        resturant.r_menu_image =  request.FILES.get('r_menu')
        resturant.r_country = cd['r_country']
        resturant.open_at =  cd['open_at']
        resturant.close_at =  cd['close_at']
        resturant.r_mobile = cd['r_mobile']
        resturant.t_location = cd['r_location']
        resturant.save()
        c = models.Country.objects.get(c_name=cd['r_country'])
        c.c_resturants.add(resturant)
        c.save()
        messages.success(request, 'the resturant has added successfully')
        return redirect('adminstration')
  


def add_country(request):
    if request.method =="POST":
        cd = request.POST
        if models.Country.objects.filter(c_name=cd['c_name']):
            messages.warning(request, 'country has added before')
            return redirect('adminstration')
        country = models.Country()
        country.c_name = cd['c_name']
        country.c_image = request.FILES.get("c_image")
        country.save()
        messages.success(request, 'the country has added successfully')
        return redirect('adminstration')



def show_countries(request):
    countries = models.Country.objects.all()
    
    
    return render(request, 'dash/countries.html', {'countries':countries})

def show_countries_details(request, id):
    country = models.Country.objects.get(id=id)
    
    return render(request, 'dash/country_details.html', {'country':country})


def delete_country(request, id):
    c = models.Country.objects.get(id=id)
    c.delete()
    messages.success(request, 'Country Deleted successfully')
    return redirect('show_countries')


import datetime

def make_hotels_reservation(request, id):
    res = Hotel_reservations()
    member = Member()
    hotel = models.Hotel.objects.get(id=id)
    cd = request.POST
    if not Member.objects.filter(m_id=cd['m_id']):

        member.m_name = cd['m_name']
        member.m_age = cd['m_age']
        member.m_mobile = cd['m_mobile']
        member.m_contact = cd['m_contact']
        member.m_id = cd['m_id']
        member.m_gender = cd['gender']
        member.save()
    else:
        member = Member.objects.filter(m_id=cd['m_id'])[0]
    
    res.member = member
    res.hotel = hotel
    res.reservation_date = cd['start_date']
    res.cancelation_date = cd['checkout']
    res.save()
    messages.success(request, 'your order has been added successfully')
    return redirect('home')


def make_trip_reservation(request, id):
    res = trip_reservations()
    member = Member()
    trip = models.Trip.objects.get(id=id)
    cd = request.POST
    if not Member.objects.filter(m_id=cd['m_id']):

        member.m_name = cd['m_name']
        member.m_age = cd['m_age']
        member.m_mobile = cd['m_mobile']
        member.m_contact = cd['m_contact']
        member.m_id = cd['m_id']
        member.m_gender = cd['gender']
        member.save()
    else:
        member = Member.objects.filter(m_id=cd['m_id'])[0]
    if trip_reservations.objects.filter(member__id=member.id, trip=trip):
        messages.warning(request, 'you already registered to this trip before contact {} for more details'.format(trip.t_mobile))
        return redirect('home')
    
    res.member = member
    res.trip = trip
    res.reservation_date = datetime.datetime.now()
    res.save()
    messages.success(request, 'your order has been added successfully')
    return redirect('home')


def make_resturant_reservation(request, id):
    res = resturant_reservations()
    member = Member()
    resturant = models.Resturant.objects.get(id=id)
    cd = request.POST
    if not Member.objects.filter(m_id=cd['m_id']):

        member.m_name = cd['m_name']
        member.m_age = cd['m_age']
        member.m_mobile = cd['m_mobile']
        member.m_contact = cd['m_contact']
        member.m_id = cd['m_id']
        member.m_gender = cd['gender']
        member.save()
    else:
        member = Member.objects.filter(m_id=cd['m_id'])[0]
  
    res.member = member
    res.resturant = resturant
    res.reservation_date = datetime.datetime.now()
    res.save()
    messages.success(request, 'your order has been added successfully')
    return redirect('home')
