from django import forms
from .models import UserInfo
	
class LoginForm(forms.Form):
	username=forms.CharField(max_length=30)
	password=forms.CharField(max_length=30,widget=forms.PasswordInput())

class SignupForm(forms.Form):
	handle=forms.CharField(max_length=30)
	password=forms.CharField(max_length=30,widget=forms.PasswordInput())
	friends= forms.CharField(widget = forms.Textarea)
