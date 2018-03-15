from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def login(request):
    return render(request,'reserve/login.html',{})