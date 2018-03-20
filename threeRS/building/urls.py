from django.urls import path, include
from .views import buildings, rooms

app_name = 'building'
urlpatterns = [
	path('', buildings, name='buildings'),
	path('<int:building_id>/', rooms, name='rooms'),
	path('<int:building_id>/<int:room_id>/', include('reservation.urls'), name='reserve'),
]