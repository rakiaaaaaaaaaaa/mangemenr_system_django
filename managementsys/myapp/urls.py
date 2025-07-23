from django.urls import path
from . import views

# define a list of URL patterns for the app
urlpatterns = [
    path('', views.index, name='index'),  
    # Add more URL patterns here as needed
    # Example: path('another/', views.another_view, name='another_view'),
]