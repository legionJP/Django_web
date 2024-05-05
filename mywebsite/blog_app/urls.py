from django.urls import path
from . import views #importing the views from current directory 

urlpatterns = [
    path('',views.home, name='blog_app-home')    #empty path for home page 
]