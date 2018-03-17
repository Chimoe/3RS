from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Building


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


