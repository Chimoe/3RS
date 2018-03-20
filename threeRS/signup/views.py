import os
from django.shortcuts import render, get_object_or_404
from .forms import SignUpForm

def signup(request):
	form = SignUpForm(request)
	return render(request, 'account.html', context={'FORM': form})
	
