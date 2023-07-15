from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from accounts.models import accounts
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import *
from .decorates import unauthenticated_user, admin_only
from .forms import accountForm, CreateUserForm


def Register(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + user)

            return redirect('Login')

    context = {'form': form}

    return render(request, "Register.html", context)


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('header')
        else:
            messages.info(request, 'username OR password is incorrect')

    context = {}

    return render(request, "Login.html", context)


@login_required(login_url='Login')
def logoutUser(request):
    logout(request)
    return redirect('Login')


@login_required(login_url='Login')
def base(request):

    return render(request, "base.html")


@login_required(login_url='Login')
def header(request):
    return render(request, "header.html")


@login_required(login_url='Login')
def wcu(request):
    return render(request, "wcu.html")


@login_required(login_url='Login')
def Explore(request):
    return render(request, "Explore.html")


@login_required(login_url='Login')
def Deliveryandpayment(request):
    return render(request, "Deliveryandpayment.html")


@login_required(login_url='Login')
def thankyou(request):
    return render(request, "thankyou.html")


@login_required(login_url='Login')
def Followus(request):
    return render(request, "Followus.html")
