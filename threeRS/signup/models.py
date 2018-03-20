import uuid
from django.db import models
from django.utils.encoding import smart_text
from phonenumber_field.modelfields import PhoneNumberField

class SignUp(models.Model):
	rin = models.IntegerField(null=True)
	# Temporarily a charField...
	password = models.CharField(max_length=20, null=True)
	email = models.EmailField(null=True)
	name = models.CharField(max_length=120, null=True)
	phone_number = PhoneNumberField(blank=True, null=True)
	fax_number = PhoneNumberField(blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	
	def __str__(self):
		return smart_text(self.name + "\t(" + self.email + ")")
	
