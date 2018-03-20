from django.urls import path
from .views import *

app_name = 'reservation'
urlpatterns = [
	path('', buildings, name='buildings'),
	path('<int:building_id>/', rooms, name='rooms'),
	path('<int:building_id>/<int:room_id>/', reserve, name='reserve'),
	path('<int:building_id>/<int:room_id>/success/', reserve_success, name='reserve_success'),
]