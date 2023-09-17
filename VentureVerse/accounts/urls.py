from django.urls import path
from .views import index,create_profile,register,login_view , dashboard,logout_view

urlpatterns = [
    path("", index, name="accounts-index"),
    path('register/',register, name='accounts-register'),
    path('select-role/',create_profile, name='accounts-select_role'),
    path('login/', login_view, name='accounts-login'),
    path('dashboard/', dashboard, name='accounts-dashboard'),
    path('logout/', logout_view, name='accounts-logout'),
]
