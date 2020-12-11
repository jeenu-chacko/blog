
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(UserCreationForm):
    email= forms.EmailField()
    name = forms.CharField()
    class Meta:
        model = User
        fields=['username','name','email','password1','password2']


class Profile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','age','image']
