from django.contrib import admin
from .models import Building, Room

class BuildingAdmin(admin.ModelAdmin):
	class Meta:
		model = Building

class RoomAdmin(admin.ModelAdmin):
	class Meta:
		model = Room
		
admin.site.register(Building)
admin.site.register(Room)