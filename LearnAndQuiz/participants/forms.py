from django import forms
from django.contrib.auth.models import User
from .models import Profile

class participants_update_form(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email']



class profile_update_form(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']
