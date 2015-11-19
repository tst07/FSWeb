from django.shortcuts import render,render_to_response
from .models import UserInfo
from django.contrib.auth import authenticate ,login,logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import LoginForm,SignupForm,ChangeForm
from django.shortcuts import render,redirect,get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.views.generic.edit import FormView
import urllib2
import json
import time
# Create your views here.

def login_view(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			usn = request.POST['username']
			pss = request.POST['password']
			user=authenticate(username=usn,password=pss)
			if user is not None:
				login(request,user)
				return HttpResponseRedirect('/welcome')
			else:
				return HttpResponseRedirect('/')
	else:
		form = LoginForm()
	return render(request,'friendsstalker/post_list.html', {'form':form})

@login_required
def welcome(request):
		star = request.user.userinfo.text
		li = star.split()
		rem = []
		ver = []
		key = []
		pnam = []
		
		
		flag = True
		for coder in li:
			#preparing url for a particular friend.Below three lines are just json and api stuff.
			#I have set count = 15 (code will track last 15 solutions of user).
			url = 'http://codeforces.com/api/user.status?handle=' + coder +'&from=1&count=15'
			json_obj = urllib2.urlopen(url)
			data = json.load(json_obj)
 
			#iterate through all x solutions of user.
			for pick in data['result']:
				#Considering Accepted solutions.
				if pick['verdict'] == "OK":
 
					#This will be used for system tests.
					if pick['testset'] == "TESTS": 
						myobj = pick['problem']
						#temp is an attempt to make a submission uniquely enter in rem. (through SubmissionID) 
						temp = str(pick['id']) + pick['verdict']
 
						if temp not in rem:
							rem.append(temp)
							if flag == True:
								ver.append("Accepted!")
								key.append(coder)
								prep  = "|" + myobj['index'] + "|" + myobj['name'] 
								pnam.append(prep)
 
					#this will be used for pretests 
					elif pick['testset']  == "PRETESTS":
						myobj = pick['problem']
						temp =  pick['id']
						if temp not in rem:
							rem.append(temp)
							ver.append("pretest-passed")
							key.append(coder)
							prep  = "|" + myobj['index'] + "|" + myobj['name'] 
							pnam.append(prep) 
 
				#this will run when non Accepted solutions.Comment everything 
				#in below else if you do not wish to see wrong submissions.
				elif pick['verdict'] != "TESTING":
					myobj = pick['problem']
					temp  = str(pick['id']) + pick['verdict']
 
					if temp not in rem:
						rem.append(temp)						
						if flag == True: 
							ver.append(pick['verdict'])
							key.append(coder)
							prep  = "|" + myobj['index'] + "|" + myobj['name'] 
							pnam.append(prep)                                               
		#we have cached all previous solutions at rem list.from now on it  
		#will detect only new submitted solutions.Used only at first iteration.
		flag = True
		
		
		#insert time according to you patience.Unit is seconds.
		fin = zip(ver,key,pnam)
		return render(request,'friendsstalker/welcome.html',{'friends':fin , 'webuser' : request.user})


def logout(request):
	auth.logout(request)
	return login_view(request)

def signup(request):
	if request.method == "POST":
		form = SignupForm(request.POST,request.FILES)
		if form.is_valid():
			a = request.POST['password']
			b = request.POST['confirm_password']
			
			if a != b:
				return HttpResponseRedirect('/signup')
			
			user=User.objects.create_user(username=request.POST['handle'],password=request.POST['password'])
									   
			user.save()
			u=UserInfo(user=user,text=request.POST['friends'])
			u.save()
			return HttpResponseRedirect('/')
	else:
		form = SignupForm()
	return render(request, 'friendsstalker/signup.html', {'form':form})

@login_required
def change_view(request):
	if request.method == "POST":
		form = ChangeForm(request.POST)
		if form.is_valid():
			request.user.userinfo.text = request.POST['friends']
			request.user.userinfo.save()
			return 	HttpResponseRedirect('/welcome')
	else:
		form = ChangeForm()
	return render(request, 'friendsstalker/change.html', {'form':form})
