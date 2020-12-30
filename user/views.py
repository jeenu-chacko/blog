from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm,ProfileForm,PostForm
from django.contrib.auth.models import User
from .models import Profile,Post



@login_required
def post_create(request):
    return render(request,'user/post_create.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            p=Profile(user=user, name=user.username)
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


def updateprofile(request,id):
    
    obj = get_object_or_404(Profile, id = id)
    form = ProfileForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return render(request, 'user/profile.html')

    return render(request, 'user/updateprofile.html',{'form':form})



def create_post(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return render(request, 'user/home.html')
    return render(request, 'user/create_post.html',{'form':form})



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    
    return render(request, 'user/home.html',context)