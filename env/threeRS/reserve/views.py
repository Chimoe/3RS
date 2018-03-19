from .models import Building
from django.shortcuts import render, get_object_or_404
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
    return render(request, 'reserve/3RS.html',{})

@login_required()
def logoutView(request):
    logout(request)
    return render(request, 'reserve/logout.html',{})

def index(request):
    building_list = Building.objects.order_by('-pub_date')
    context = {'building_list': building_list}
    return render(request, 'reserve/index.html', context)


def detail(request, building_id):
    building = get_object_or_404(Building, pk=building_id)
    return render(request, 'reserve/detail.html', {'building': building})


def results(request, building_id):
    response = "You're looking at the results of building %s."
    return HttpResponse(response % building_id)


def take(request, building_id):
    return HttpResponse("You're taking a room in building %s." % building_id)
