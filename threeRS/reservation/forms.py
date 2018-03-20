from django import forms
# Models
from .models import Reservation

class ReservationForm(forms.ModelForm):
	class Meta:
		model = Reservation
		fields = ['event_name', 'room', 'date', 'time_begin', 'time_end', 'room',
				  'attendance']

#class ReservationUpdate(forms.Form):
	