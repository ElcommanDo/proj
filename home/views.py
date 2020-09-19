from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home/index.html', {})


def about(request):
    return render(request, 'home/about.html', {})


def destinations(request):
    return render(request, 'home/travel_destination.html', {})

    
def contact(request):
    return render(request, 'home/contact.html', {})


