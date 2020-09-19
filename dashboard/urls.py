from django.urls import path
from . import views


urlpatterns = [
    path('login-adminstration/', views.login_admin, name='login'),
    path('adminstration-profile/',views.adminstration, name='adminstration'),
    path('logout-adminstration/', views.logout_admin, name='logout'),

]