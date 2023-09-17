from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import RoleSelectionForm
from .models import EmployeeProfile, EmployerProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

def index(request):
    return render(request, 'index.html')


def create_profile(request):
    if request.method == 'POST':
        form = RoleSelectionForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data['role']
            user = request.user

            if role == 'employee':
                EmployeeProfile.objects.create(user=user)
            elif role == 'employer':
                EmployerProfile.objects.create(user=user)

            return redirect('profile_created_successfully')

    else:
        form = RoleSelectionForm()

    return render(request, 'accounts/select_role.html', {'form': form})

def register(request):
    if request.user.is_authenticated:
        # If the user is already authenticated, redirect to the dashboard
        return redirect('accounts-dashboard')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts-select_role')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accounts-dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

logout_view = LogoutView.as_view()

@login_required
def dashboard(request):
    user = request.user
    user_data = {
        'username': user.username,
        'email': user.email,
    }
    return render(request, 'accounts/dashboard.html', {'user_data': user_data})

logout_view = LogoutView.as_view()

