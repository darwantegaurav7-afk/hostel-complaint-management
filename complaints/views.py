from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import ComplaintForm
from .models import Complaint

# 1. Registration System
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Account bante hi login ho jayega
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# 2. Login System
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# 3. Logout System
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

# 4. Home Page (Sirf Login wale students ke liye)
@login_required(login_url='login') # Yeh line bina login walo ko bahar kar degi
def home(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.student = request.user # Jisne login kiya hai, uska naam automatically save hoga
            complaint.save()
            return redirect('home')
    else:
        form = ComplaintForm()
    
    # Sirf us student ki complaints dikhao jisne login kiya hai
    user_complaints = Complaint.objects.filter(student=request.user)
    
    return render(request, 'home.html', {'form': form, 'complaints': user_complaints})