from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.db.models import Avg
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
#cross-site request forgery 
#from social.models import User, Dream, UserForm, UserProfileForm, DreamSubmission
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from models import User, UserForm, Evaluation, UserProfile, Team
from django.core.validators import MaxValueValidator, MinValueValidator

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/home')

def home(request):
	return render(request, 'home.html', {})

@login_required
def confirmation(request):
	return render(request, 'confirmation.html', {})

@login_required
def loggedin(request):
	return render(request, 'loggedin.html', {})

def invalid(request):
	return render(request, 'invalid.html', {})

def forgot(request):
    return render(request, 'forgot.html', {})

@login_required
def register(request):
        return render(request, 'register.html', {})

@login_required
def recentsub(request):
    return render(request, 'recentsub.html',
        {'evaluations': Evaluation.objects.all})

class EvaluationForm(forms.Form):
    author = forms.CharField(label = "Username", initial="NOOOO")
    author.widget = author.hidden_widget()
    evaluee = forms.ModelChoiceField(required = True, label = "Evaluee", queryset=User.objects.all().order_by('username'))
    participation = forms.IntegerField(required = True, label = "Participation" , validators=[MinValueValidator(1), MaxValueValidator(10)])
    communication = forms.IntegerField(required = True, label = "Communication" , validators=[MinValueValidator(1), MaxValueValidator(10)])
    presentation = forms.IntegerField(required = True, label = "Presentation" , validators=[MinValueValidator(1), MaxValueValidator(10)])
    techskill = forms.IntegerField(required = True, label = "Technical Skill" , validators=[MinValueValidator(1), MaxValueValidator(10)])

class TeamForm(forms.Form):
    teamName = forms.IntegerField(label="Team Name")
    member1 = forms.ModelChoiceField(required = True, label = "Member 1", queryset=User.objects.all().order_by('username'))
    member2 = forms.ModelChoiceField(required = True, label = "Member 2", queryset=User.objects.all().order_by('username'))
    member3 = forms.ModelChoiceField(required = True, label = "Member 3", queryset=User.objects.all().order_by('username'))
    member4 = forms.ModelChoiceField(required = False, label = "Member 4", queryset=User.objects.all().order_by('username'))
    member5 = forms.ModelChoiceField(required = False, label = "Member 5", queryset=User.objects.all().order_by('username'))

class EvalForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        exclude = ('author', 'evaluee')

def edit_eval(request, id):
    instance = Evaluation.objects.get(id=id)
    form = EvalForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/confirmation')
    return render(request, 'editEval.html', {'form': form})


@login_required
def evaluation(request):
    if request.method == 'POST':
        form = EvaluationForm(request.POST)
        if form.is_valid():
            ev = Evaluation()
            ev.author = form.cleaned_data["author"] = request.user
            ev.evaluee = form.cleaned_data["evaluee"]
            ev.participation = form.cleaned_data["participation"]
            ev.communication = form.cleaned_data["communication"]
            ev.presentation = form.cleaned_data["presentation"]
            ev.techskill = form.cleaned_data["techskill"]
            ev.save()
            return HttpResponseRedirect ("/confirmation")
    elif request.method == 'GET':
        form = EvaluationForm()
    else:
        return HttpResponseRedirect ("/404/")
    return render(request, 'evaluation.html', {"form": form, "teams": Team.objects.all})

@login_required
def registerTeam(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            rt = Team()
            rt.teamName = form.cleaned_data["teamName"]
            rt.member1 = form.cleaned_data["member1"]
            rt.member2 = form.cleaned_data["member2"]
            rt.member3 = form.cleaned_data["member3"]
            rt.member4 = form.cleaned_data["member4"] or None
            rt.member5 = form.cleaned_data["member5"] or None
            rt.save()
            return HttpResponseRedirect ("/confirmation")
    elif request.method == 'GET':
        form = TeamForm()
    else:
        return HttpResponseRedirect ("/404/")
    return render(request, 'registerTeam.html', {"form": form, "teams": Team.objects.all().order_by("teamName")})

@login_required
def statistics(request):
    if request.user.is_authenticated():
        average = Evaluation.objects.aggregate(Avg('participation'), Avg('communication'), Avg('presentation'), Avg('techskill'))
        return render(request, 'statistics.html',
                     {'users': User.objects.all,
                      'evaluations': Evaluation.objects.all,
                      'partavg': Evaluation.objects.aggregate(Avg('participation')),
                      'commavg': Evaluation.objects.aggregate(Avg('communication')),
                      'presavg': Evaluation.objects.aggregate(Avg('presentation')),
                      'techavg': Evaluation.objects.aggregate(Avg('techskill')),
                      'totalavg': average})
    else:
        return HttpResponseRedirect('/home/')


def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        
        if user:
            # Is the account active? 
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/loggedin')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your MyStupidDreams account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponseRedirect('/invalid')
    else:
        return render(request, 'login.html', {})

def submit_evaluation(request):
    if request.method == 'POST':
        eval1 = EvaluationForm(request.POST)
        if eval1.is_valid():
            x = Evaluation()
            x.participation = eval1.cleaned_data["participation"]
            x.communication = eval1.cleaned_data["communication"]
            x.presentation = eval1.cleaned_data["presentation"]
            x.techskill = eval1.cleaned_data["techskill"]
            x.save()
            return HttpResponseRedirect("/valid_submission")
    else:
        eval1 = EvaluationForm()
    return render(request, "loggedin.html", {"eval1": eval1})
    

@login_required
def register(request):
        registered = False
        if request.method == 'POST':
                user_form = UserForm(data=request.POST)

                if user_form.is_valid():
                        user = user_form.save()
                        user.set_password(user.password)
                        user.save()

                        registered = True

                else:
                        print(user_form.errors)

        else:
                user_form = UserForm()

        return render(request,
                      'register.html',
                      {'user_form': user_form, 'registered': registered})

                        

