from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
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
    return render(request, 'dash/admin.html', {})



def logout_admin(request):
    logout(request)
    messages.success(request, 'logout has made successfully')
    return redirect('home')
    