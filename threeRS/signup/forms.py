from django import forms
import datetime
# Models
from .models import SignUp
	
class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['rin', 'password', 'email', 'name',
				  'phone_number', 'fax_number']