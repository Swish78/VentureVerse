from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import EmployeeProfile, EmployerProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RoleSelectionForm, EmployeeRegistrationForm, EmployerRegistrationForm


def index(request):
    if request.user.is_authenticated:
        # If the user is already authenticated, redirect to the dashboard
        return redirect('accounts-dashboard')

    # Display the index page with registration/login links
    return render(request, 'index.html')
def select_role(request):
    if request.user.is_authenticated:
        # If the user is already authenticated, redirect to the dashboard
        return redirect('accounts-dashboard')

    if request.method == 'POST':
        form = RoleSelectionForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data['role']
            # Store the selected role in the session
            request.session['selected_role'] = role
            if role == 'employee':
                return redirect('accounts-employee-registration')
            elif role == 'employer':
                return redirect('accounts-employer-registration')
    else:
        form = RoleSelectionForm()

    return render(request, 'accounts/select_role.html', {'form': form})



def employee_registration(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            selected_role = request.session.get('selected_role')
            # Process and save employee registration data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            experience = form.cleaned_data['experience']
            dob = form.cleaned_data['DOB']
            password = form.cleaned_data['password']  # Add password field

            # Create a new user object
            user = User.objects.create_user(username=email, email=email, password=password)

            # Create an EmployeeProfile associated with the user
            employee_profile = EmployeeProfile(user=user)
            employee_profile.save()

            # You can update the user model with additional fields if needed
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            # After successful registration, you can redirect to a success page
            return redirect('accounts-registration-success')
    else:
        form = EmployeeRegistrationForm()

    return render(request, 'accounts/employee_registration.html', {'form': form})


def employer_registration(request):
    if request.method == 'POST':
        form = EmployerRegistrationForm(request.POST)
        if form.is_valid():
            selected_role = request.session.get('selected_role')
            # Process and save employer registration data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            company_name = form.cleaned_data['company_name']
            industry = form.cleaned_data['industry']
            employee_count = form.cleaned_data['employee_count']
            location = form.cleaned_data['location']
            password = form.cleaned_data['password']  # Add password field

            # Create a new user object
            user = User.objects.create_user(username=email, email=email, password=password)

            # Create an EmployerProfile associated with the user
            employer_profile = EmployerProfile(user=user)
            employer_profile.save()

            # You can update the user model with additional fields if needed
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            # After successful registration, you can redirect to a success page
            return redirect('accounts-registration-success')
    else:
        form = EmployerRegistrationForm()

    return render(request, 'accounts/employer_registration.html', {'form': form})

# @login_required
# def create_profile(request):
#     if request.method == 'POST':
#         form = RoleSelectionForm(request.POST)
#         if form.is_valid():
#             role = form.cleaned_data['role']
#             user = request.user  # Get the authenticated user
#
#             if role == 'employee':
#                 EmployeeProfile.objects.create(user=user)
#             elif role == 'employer':
#                 EmployerProfile.objects.create(user=user)
#
#             return redirect('profile_created_successfully')
#
#     else:
#         form = RoleSelectionForm()
#
#     return render(request, 'accounts-select_role.html', {'form': form})
#
def register(request):
    if request.user.is_authenticated:
        # If the user is already authenticated, redirect to the dashboard
        return redirect('accounts-dashboard')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # Store the selected role in the session
            request.session['selected_role'] = request.POST.get('role')

            return redirect('accounts-select_role')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


def dashboard(request):
    user = request.user
    user_data = {
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }
    selected_role = request.session.get('selected_role')
    user_data['selected_role'] = selected_role

    return render(request, 'accounts/dashboard.html', {'user_data': user_data})

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

def registration_success(request):
    # Retrieve the selected role from the session
    selected_role = request.session.get('selected_role')
    user_data = {
        'selected_role': selected_role,
    }
    return render(request, 'accounts/registration_success.html', {'user_data': user_data})



