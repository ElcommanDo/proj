from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    path('detinations-details/',views.destinations, name='destinations'),
    path('contact-us/',views.contact, name='contact'),
    
    

]