from django.urls import path
from . import views


urlpatterns = [
    path('login-adminstration/', views.login_admin, name='login'),
    path('adminstration-profile/',views.adminstration, name='adminstration'),
    path('logout-adminstration/', views.logout_admin, name='logout'),
 
    path('add-hotel/', views.add_hotel, name='add_hotel'),
    path('add-resturant/', views.add_resturant, name='add_resturant'),
    path('add-trip/', views.add_trip, name='add_trip'),
    path('add-country/', views.add_country, name='add_country'),
    path('show_countries/', views.show_countries, name='show_countries'),
    path('delete-country/<int:id>/', views.delete_country, name='delete_country'),
    path('show_countries_details/<int:id>/', views.show_countries_details, name='show_countries_details'),
    path('trip-reservations/<int:id>/', views.make_trip_reservation, name='trip_reservation'),
    path('hotels-reservations/<int:id>/', views.make_hotels_reservation, name='hotel_reservation'),
    path('resturant-reservations/<int:id>/', views.make_resturant_reservation, name='resturant_reservation'),
    
    
    

]