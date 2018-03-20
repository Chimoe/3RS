from django.contrib import admin
from .models import Building, Room, Reservation

class BuildingAdmin(admin.ModelAdmin):
	class Meta:
		model = Building

class RoomAdmin(admin.ModelAdmin):
	class Meta:
		model = Room
		

class ReservationAdmin(admin.ModelAdmin):
	class Meta:
		model = Reservation
		
admin.site.register(Building)
admin.site.register(Room)
admin.site.register(Reservation)