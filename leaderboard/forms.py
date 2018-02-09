#from django.contrib.auth.models import User
from django import forms
from .models import LadderUser, Team_12v12

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = LadderUser
        fields = ['username', 'email', 'password', 'profile_pic']



class RegisterTeam12v12(forms.ModelForm):
    
    class Meta:
        model = Team_12v12
        fields = ['team_name', 'logo', 'bio']


        