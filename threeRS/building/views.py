from django.shortcuts import render, get_object_or_404
from .models import Building, Room

def buildings(request):
	all_buildings = Building.objects.order_by('id')
	context = { 'all_buildings' : all_buildings, }
	return render(request, 'buildings.html', context)

def rooms(request, building_id):
	building = Building.objects.filter(id=building_id)
	available_rooms = Room.objects.filter(building=building_id).filter(reserved=False)
	context = { 'building' : building,
		'available_rooms' : available_rooms,
		}
	return render(request, 'rooms.html', context)