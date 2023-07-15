
from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.header, name='header'),
    path('Login/', views.Login, name='Login'),

    path('wcu/', views.wcu, name='wcu'),
    path('Explore/', views.Explore, name='Explore'),
    path('Deliveryandpayment/', views.Deliveryandpayment,
         name='Deliveryandpayment'),
    path('Followus/', views.Followus, name='Followus'),
    path('logout/', views.logoutUser, name='logout'),
    path('Register/', views.Register, name='Register')

]
