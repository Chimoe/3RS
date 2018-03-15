from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def login(request):
    return render(request,'reserve/login.html',{})

def home(request):
    return render(request, 'reserve/home.html',{})

