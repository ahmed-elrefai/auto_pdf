from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,get_user_model, logout as auth_logout, login as auth_login
from django.contrib import messages
from core.views import home

# Create your views here.
User = get_user_model()

def logout(request):
    auth_logout(request)
    return redirect('login')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, "accounts/login.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('signup')
        
        user = User.objects.create_user(username=username, password=password)
        auth_login(request, user)

        return redirect('home')
    
    return render(request, "accounts/signup.html")
