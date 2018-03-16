from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return home(request)
    else:
        return HttpResponseNotFound("Invalid Login")

@login_required()
def home(request):
    return render(request, 'reserve/home.html',{})

@login_required()
def logoutView(request):
    logout(request)
    return render(request, 'reserve/logout.html',{})