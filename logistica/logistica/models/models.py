##from django.db import models
##from django.contrib.auth.models import User
##from django import forms
##
##
##
##class UserProfile(models.Model):
##    user = models.OneToOneField(User)
##    username = models.CharField(max_length = 30)
##    email = models.EmailField(default = "")
##    password = models.CharField(max_length = 30)
##    picture = models.ImageField(upload_to='social/static/profile_images', blank=True)
##
##    def __unicode__(self):
##        return self.user.username
##    def getusername(self):
##        return self.username
##
##
##class UserForm(forms.ModelForm):
##    password = forms.CharField(widget=forms.PasswordInput())
##    class Meta:
##        model = User
##        fields = ('username', 'email', 'password')
##
##class UserProfileForm(forms.ModelForm):
##    class Meta:
##        model = UserProfile
##        fields = ('picture',)
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
