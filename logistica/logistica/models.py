from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

##class LoginForm(forms.Form):
##	username = forms.CharField(label='Username', max_length=30)
##	password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput) 
    


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length = 30)
    #email = models.EmailField(default = "")
    password = models.CharField(max_length = 30)
    #picture = models.ImageField(upload_to='social/static/profile_images', blank=True)

    def __unicode__(self):
        return self.user.username
    def getusername(self):
        return self.username


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password')


class Evaluation(models.Model):
    participation = models.IntegerField(max_length=2,
                                        default = 5)
    communication = models.IntegerField(max_length=2,
                                        default = 5)
    presentation = models.IntegerField(max_length=2,
                                        default = 5)
    techskill = models.IntegerField(max_length=2,
                                        default = 5)
    
class EvaluationForm(forms.Form):
    participation = forms.IntegerField(label = "Participation")
    
##class EvaluationForm(forms.ModelForm):
##        class Meta:
##            model = Evaluation
##            fields = ['participation', 'communication', 'presentation', 'techskill']
##
##class UserProfileForm(forms.ModelForm):
##    class Meta:
##        model = UserProfile
##        #fields = ('picture',)
##        
##
##class Dream(models.Model):
##    title = models.CharField(max_length = 120)
##    content = models.CharField(max_length = 1000)
##    user = models.ForeignKey('UserProfile')
##    flock = models.CharField(max_length = 32)
##
##class DreamSubmission(forms.ModelForm):
##    class Meta:
##        model = Dream
##        fields = ('title', 'content', 'flock', 'user')
##
##class Search(models.Model):
##    dream_search = models.CharField(max_length = 30)
