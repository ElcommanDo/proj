from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    path('contact-us/',views.contact, name='contact'),
    path('travel-destinations/', views.travel_destinations, name='travel_destinations'),
    path('search/',views.search, name='search'),
    path('Hotels-searching/',views.hotels_search, name='hotels_search'),
    path('hotels_destinations/', views.hotels_destinations, name='hotels_destinations'),
    path('resturant_destinations/', views.resturant_destinations, name='resturant_destinations'),
    path('resturant-searching/',views.resturant_search, name='resturant_search'),
    path('member_reservations/', views.member_reservations, name='member_reservations'),
    

]