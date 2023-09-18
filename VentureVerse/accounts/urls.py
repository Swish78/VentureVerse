from django.urls import path
from .views import index,login_view , dashboard,logout_view, employee_registration, employer_registration,select_role,registration_success
urlpatterns = [
    path("", index, name="index"),
    path('select-role/', select_role, name='accounts-select_role'),
    path('employee-registration/', employee_registration, name='accounts-employee-registration'),
    path('employer-registration/', employer_registration, name='accounts-employer-registration'),
    path('login/', login_view, name='accounts-login'),
    path('dashboard/', dashboard, name='accounts-dashboard'),
    path('logout/', logout_view, name='accounts-logout'),
    path('registration-success/', registration_success, name='accounts-registration-success'),

]
