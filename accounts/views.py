from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.

def signupView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})

def signinView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('login')
    else: 
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form':form})

def signoutView(request):
    logout(request)
    messages.success(request,'You have successfully logged out!')
    return redirect('home')