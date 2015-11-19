from django import forms
from .models import UserInfo
from django.contrib.auth.models import User
	
class LoginForm(forms.Form):
	username=forms.CharField(max_length=30)
	password=forms.CharField(max_length=30,widget=forms.PasswordInput())

class SignupForm(forms.Form):
	handle=forms.CharField(max_length=30)
	password=forms.CharField(max_length=30,widget=forms.PasswordInput())
	confirm_password=forms.CharField(max_length=30,widget=forms.PasswordInput())
	friends= forms.CharField(widget = forms.Textarea)

class ChangeForm(forms.Form):
	friends= forms.CharField(widget = forms.Textarea)
