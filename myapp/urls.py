from django.urls import path
from . import views

# define a list of URL patterns for the app
urlpatterns = [
   
    path('home/', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    # Add more URL patterns here as needed
    # Example: path('another/', views.another_view, name='another_view'),
]