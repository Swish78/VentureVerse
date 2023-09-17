from django.urls import path
from .views import index

urlpatterns = [
    path("", index, name="accounts-index"),  # Example URL mapping
    # Add more URL patterns for your app as needed
]
