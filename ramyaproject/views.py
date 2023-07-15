from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import authenticate
from django.contrib import messages


def Register(request):

    context = {}
    return render(request, "Register.html", context)


def base(request):

    return render(request, "base.html")


def header(request):

    return render(request, "header.html")


def wcu(request):
    return render(request, "wcu.html")


def Explore(request):
    return render(request, "Explore.html")


def Deliveryandpayment(request):
    return render(request, "Deliveryandpayment.html")


def thankyou(request):
    return render(request, "thankyou.html")


def Followus(request):
    return render(request, "Followus.html")


def Login(request):
    context = {}
    return render(request, "Login.html", context)


def Logout(request):
    return redirect('Login')


def Signup(request):
    return render(request, "Signup.html")
