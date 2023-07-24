from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Logged in successfully..")
            return redirect('home')
        else:
            messages.error(request, "Please check your credentials..")
            return render(request, 'home.html')

    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out..")
    return redirect('home')
    

