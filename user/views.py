from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm
from django.contrib.auth.models import User
from .models import Profile



@login_required
def success(request):
    return render(request,'user/dashboard.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            p=Profile(user=user, name=user.name)
            p.save()
            login(request, user)
            return redirect('success')
        else:
            return render(request, 'user/login.html', {'form': form})
    else:
        form = CustomUserForm()
        return render(request, 'user/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('success')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def profile(request): 
    return render(request, 'user/profile.html')


def updateprofile(request):
    form = Profile()
    return render(request, 'user/profile.html',{'form':form})