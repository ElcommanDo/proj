from django.shortcuts import render
from dashboard.models import Country, Hotel, Trip, Resturant, Member
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
    if not cd['location']  or cd['country']:
        resturants = Resturant.objects.all()     
        countries = Country.objects.all()
        locations = [x.t_location for x in resturants]
        return render(request, 'home/resturants_search.html', {'resturants':resturants, 'countries':countries,'locations':locations})

   
    country = Country.objects.get(c_name=cd['country'])
    
    resturants = [x for x in country.c_resturants.all() if x.t_location == cd['location'] and  x.r_country == cd['country']]
    countries = Country.objects.all()
    return render(request, 'home/resturants_search.html', {'resturants':resturants, 'countries':countries})

def search(request):
    cd= request.POST
    if not cd['from_price'] or cd['to_price'] or cd['country']:
        trips = Trip.objects.all()     
        countries = Country.objects.all()
        return render(request, 'home/travel_destination.html', {'trips':trips, 'countries':countries})

   
    country = Country.objects.get(c_name=cd['country'])
    
    trips = [x for x in country.c_trips.all() if x.t_price >= int(cd['from_price']) and  x.t_price <= int(cd['to_price'])]
    countries = Country.objects.all()
    return render(request, 'home/travel_destination.html', {'trips':trips, 'countries':countries})


def hotels_search(request):
    cd= request.POST
    

    
    if  not  cd['from'] or cd['to'] or cd.get("count"):
        hotels = Hotel.objects.all()     
        countries = Country.objects.all()
        return render(request, 'home/hotels_search.html', {'hotels':hotels, 'countries':countries})

        

    print('hhhhhhhhhhhhhhhhhhhhhh')
   
    country = Country.objects.get(c_name=cd['count'])
    hotels = [x for x in country.c_hotels.all() if x.r_price >= int(cd['from']) and  x.r_price <= int(cd['to'])]
    countries = Country.objects.all()
    return render(request, 'home/hotels_search.html', {'hotels':hotels, 'countries':countries})

