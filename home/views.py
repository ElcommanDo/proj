from django.shortcuts import render
from dashboard.models import Country, Hotel, Trip, Resturant, Member, trip_reservations, Hotel_reservations, resturant_reservations
# Create your views here.


def home(request):
    countries = Country.objects.all()
    trips = Trip.objects.all()
    hotels = Hotel.objects.all()
    resturants = Resturant.objects.all()
    
    return render(request, 'home/index.html', {'countries':countries,'resturants':resturants,
     'hotels':hotels,'trips':trips})


def about(request):
    return render(request, 'home/about.html', {})


    
def contact(request):
    return render(request, 'home/contact.html', {})



def travel_destinations(request):
    trips = Trip.objects.all()
    countries = Country.objects.all()
    context = {'trips':trips, 'countries':countries}
    return render(request, 'home/travel_destination.html', context)

def hotels_destinations(request):
    hotels = Hotel.objects.all()
    countries = Country.objects.all()
    context = {'hotels':hotels, 'countries':countries}
    return render(request, 'home/hotels_search.html', context)

def resturant_destinations(request):
    resturants = Resturant.objects.all()
    countries = Country.objects.all()
    locations = [x.t_location for x in resturants]
    context = {'resturants':resturants, 'countries':countries,'locations':locations}
    return render(request, 'home/resturants_search.html', context)

def resturant_search(request):
    cd= request.POST
    country = Country.objects.get(c_name=cd['country'])
    resturants = [x for x in country.c_resturants.all() if x.t_location == cd['location'] and  x.r_country == cd['country']]
    countries = Country.objects.all()
    return render(request, 'home/resturants_search.html', {'resturants':resturants, 'countries':countries})

def search(request):
    cd= request.POST
    country = Country.objects.get(c_name=cd['country'])
    print(cd)
    trips = [x for x in country.c_trips.all() if x.t_price >= int(cd['from_price']) and  x.t_price <= int(cd['to_price'])]
    countries = Country.objects.all()
    return render(request, 'home/travel_destination.html', {'trips':trips, 'countries':countries})


def hotels_search(request):
    cd= request.POST
    country = Country.objects.get(c_name=cd['count'])
    hotels = [x for x in country.c_hotels.all() if x.r_price >= int(cd['from']) and  x.r_price <= int(cd['to'])]
    countries = Country.objects.all()
    return render(request, 'home/hotels_search.html', {'hotels':hotels, 'countries':countries})



def member_reservations(request):
    if request.method == "POST":
        cd = request.POST
        tres = trip_reservations.objects.filter(member__m_id=cd['m_id'])
        hres = Hotel_reservations.objects.filter(member__m_id=cd['m_id'])
        rres = resturant_reservations.objects.filter(member__m_id=cd['m_id'])
        context = {'tres':tres, 'hres':hres, 'rres': rres} 
        return render(request, 'home/member_reservations.html', context )
    return render(request, 'home/member_reservations.html')

