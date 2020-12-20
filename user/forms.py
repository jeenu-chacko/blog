
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(UserCreationForm):
    email= forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    class Meta:
        model = User
        fields=['username','name','email','password1','password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','age','gender','linkedin_Url','image']
