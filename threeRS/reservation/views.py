from django.shortcuts import render, get_object_or_404
from .models import Building, Room, Reservation
from django.http import HttpResponseNotFound
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def buildings(request):
	buildings = Building.objects.order_by('name')
	context = { 'buildings' : buildings, }
	return render(request, 'buildings.html', context)

def rooms(request, building_id):
	b = get_object_or_404(Building, id=building_id)
	available_rooms = Room.objects.filter(building=b).filter(reserved=False)
	context = { 'building' : b,
		'available_rooms' : available_rooms,
		}
	return render(request, 'rooms.html', context)

def reserve(request, building_id, room_id):
	b = get_object_or_404(Building, id=building_id)
	queryset = Room.objects.filter(building=b)
	r = get_object_or_404(queryset, id=room_id)
	return render(request, 'reserve.html',
				  { 'building': b,
				    'room': r, })
	
def reserve_success(request, building_id, room_id):
	b = get_object_or_404(Building, id=building_id)
	r = get_object_or_404(Room, building=b, id=room_id)
	try:
		event_name = str(request.POST['event_name'])
		date = request.POST['date']
		time_begin = request.POST['time_begin']
		time_end = request.POST['time_end']
		attendance = int(request.POST['attendance'])
	except (KeyError):
		context = { 'building': b,
				   'room': r,
				   'error_message': 'Fill Out Missing Information', }
		return render(request, 'reserve.html', context)
	else:
		r.reserved = True;
		r.save()
		reservation = Reservation(building=b,
								  room=r,
								  event_name=event_name,
								  date=date,
								  time_begin=time_begin,
								  time_end=time_end,
								  attendance=attendance)
		reservation.save()
		context = { 'building': b,
				   'room': r,
				   'success': 'You made a reservation for ' + str(r), }
		return render(request, 'reserve.html', context)

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