from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm, AddRecordForm
from .models import Record

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
    if request.user.is_authenticated:
        records = Record.objects.all()
        return render(request, 'home.html', {'records': records})
    return render(request, 'home.html')

# register view using UserCreationForm
def signup_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Login after registration
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user:
                # User is authenticated
                login(request, user)
                messages.success(request,"Account registered successfully")
                return redirect('home')
    else:
        form = RegisterForm()
        return render(request, 'signup.html', {'form': form})
        
    return render(request, 'signup.html', {'form': form})


# manual register view
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.error(request,'username already exists..')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'email already registered..')
            return redirect('register')
        if password1 != password2:
            messages.error(request, 'passwords didn\'t match..')
            return redirect('register')
        user = User.objects.create_user(username=username,email=email, password=password1)
        messages.success(request, "Registered Successfully, Login with your credentials...")
        return redirect('home')
    return render(request, 'register.html')

        
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out..")
    return redirect('home')


def view_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(pk=pk)
        return render(request, 'record_detail.html', {'record':record})
    return redirect('home')

def add_record(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddRecordForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Record has been added..")
                return redirect('home')
            return render(request, 'add_record.html', {'form': form})
        else:
            form = AddRecordForm()
            return render(request, 'add_record.html', {'form': form})

def delete_record(request, pk):
    if request.user.is_authenticated:       
        delete_record = Record.objects.get(pk=pk)
        delete_record.delete()
        messages.success(request, 'Record has been deleted.')
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        update_record = Record.objects.get(pk=pk)
        
        if request.method == "POST":
            form = AddRecordForm(request.POST, instance=update_record)
            if form.is_valid():
                form.save()
                messages.success(request, 'Record has been updated.')
                return redirect('home')
            else:
                form = AddRecordForm(request.POST)
                return render(request, 'update_record.html', {'form':form, 'record':update_record})

        form = AddRecordForm(instance=update_record)
        return render(request, 'update_record.html', {'form':form, 'record':update_record})





    

