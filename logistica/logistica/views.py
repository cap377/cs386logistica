from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
#cross-site request forgery 
#from social.models import User, Dream, UserForm, UserProfileForm, DreamSubmission
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from models import LoginForm


##@login_required
##def user_logout(request):
##    # Since we know the user is logged in, we can now just log them out.
##    logout(request)
##
##    # Take the user back to the homepage.
##    return HttpResponseRedirect('/home')


def home(request):
	return render(request, 'home.html', {})
def login(request):
	error = ""
	if request.method == "POST":
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			username = login_form.cleaned_data["username"]
			password = login_form.cleaned_data["password"]
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return HttpResponseRedirect('/home/')
			else:
				error = "Invalid username/password."
				form = LoginForm(initial={'username': request.POST.get('username')})
	elif request.method == 'GET':
		login_form = LoginForm()
	else:
		return HttpResponseRedirect('/login/')
	return render(request, "login.html", {'login_form': login_form, 'error': error })
##@login_required
##def dream_info(request):
##        return render(request, 'dreams.html', {
##                'user_dreams': User.objects.all(),
##                'dreams': Dream.objects.all()})
##
##@login_required
##def dreamuser_info(request, usernamen):
##        dreamlist = Dream.objects.all().filter(user__username = usernamen)
##	return render(request, 'dreams.html', {'dreams' : dreamlist})
##
##@login_required
##def flock_info(request):
##	return render(request, 'flock.html', {'user_dreams' : User.objects.all(), 'dreams' : Dream.objects.all(),
##                                               'flocks' : Dream.objects.values('flock').distinct()})
##
##
##def about(request):
##	return render(request, 'about.html', {})
##
##
##def invalid_login(request):
##    return render(request, 'invalid_login.html', {})
##
##
##def user_login(request):
##
##    # If the request is a HTTP POST, try to pull out the relevant information.
##    if request.method == 'POST':
##        # Gather the username and password provided by the user.
##        # This information is obtained from the login form.
##                
##        username = request.POST.get('username')
##        password = request.POST.get('password')
##
##        
##        # combination is valid - a User object is returned if it is.
##        user = authenticate(username=username, password=password)
##
##        # If we have a User object, the details are correct.
##        
##        if user:
##            # Is the account active? 
##            if user.is_active:
##                # If the account is valid and active, we can log the user in.
##                # We'll send the user back to the homepage.
##                login(request, user)
##                return HttpResponseRedirect('/dreams/')
##            else:
##                # An inactive account was used - no logging in!
##                return HttpResponse("Your MyStupidDreams account is disabled.")
##        else:
##            # Bad login details were provided. So we can't log the user in.
##            print("Invalid login details: {0}, {1}".format(username, password))
##            return HttpResponseRedirect('/invalid_login/')
##    else:
##        return render(request, 'login.html', {})
##
##
##
##												 
##def auth_view(request):
##	username = request.POST.get('username', '')
##	password = request.POST.get('password', '')
##	#empty string on the end basically means if you can't find some value at least return an invalid error
##	user = auth.authenticate(username=username, password=password)
##
##	if user is not None:
##		auth.login(request, user)
##		return HttpResponseRedirect('loggedin')
##	else:
##		return HttpResponseRedirect('invalid')
##
##
##def register(request):
##        registered = False
##        if request.method == 'POST':
##                user_form = UserForm(data=request.POST)
##                profile_form = UserProfileForm(data=request.POST)
##
##                if user_form.is_valid() and profile_form.is_valid():
##                        user = user_form.save()
##                        user.set_password(user.password)
##                        user.save()
##                        
##                        profile = profile_form.save(commit=False)
##                        profile.user = user
##
##                        if 'picture' in request.FILES:
##                                profile.picture = request.FILES['picture']
##
##                        profile.save()
##
##                        registered = True
##
##                else:
##                        print(user_form.errors, profile_form.errors)
##
##        else:
##                user_form = UserForm()
##                profile_form = UserProfileForm()
##
##        return render(request,
##                      'register.html',
##                      {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})
##
##                        
##@login_required
##def submit(request):
##    if request.method == 'POST':
##        form2 = DreamSubmission(request.POST)
##        if form2.is_valid():
##            x = Dream()
##            x.title = form2.cleaned_data["title"]
##            x.content = form2.cleaned_data["content"]
##            x.flock = form2.cleaned_data["flock"]
##            x.user = form2.cleaned_data["user"]
##            x.save()
##            return HttpResponseRedirect("/dreams/")
##    elif request.method == 'GET':
##        form2 = DreamSubmission()
##    else:
##        return HttpResponseRedirect("/404/")
##    return render(request, "submitdream.html", {"form2": form2})
